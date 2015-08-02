# -*- coding: utf-8 -*-
import re
from django.core.urlresolvers import reverse
from django.db.models.query_utils import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.translation import get_language
from django.views.decorators.csrf import csrf_exempt
from fs_ref.api.util import login_or_token_required, render_json
from fs_ref.app.references.models import Reference, Market, Type, FilterSolution, Manufacturer, EnglishTranslation
from functools import wraps


def jsonp(f):
    @wraps(f)
    def jsonp_wrapper(request, *args, **kwargs):
        resp = f(request, *args, **kwargs)
        if resp.status_code != 200:
            return resp
        if 'callback' in request.GET:
            callback = request.GET['callback']
            resp['Content-Type'] = 'text/javascript; charset=utf-8'
            resp.content = "%s(%s)" % (callback, resp.content)
            return resp

        elif 'jsonp' in request.GET:
            callback = request.GET['jsonp']
            resp['Content-Type'] = 'text/javascript; charset=utf-8'
            resp.content = "%s(%s)" % (callback, resp.content)
            return resp
        else:
            return resp

    return jsonp_wrapper


@jsonp
def list_references(request):
    if get_language() == 'en':
        data_list = [item.to_dict() for item in EnglishTranslation.objects.filter(
            reference__is_approved=True,
            reference__is_published=True
        )]
    else:
        data_list = [item.to_dict() for item in Reference.objects.filter(is_approved=True, is_published=True)]

    return render_json(object=data_list)


@login_or_token_required()
def add_references(request):
    pass


def fetch_reference(request, id):
    object = get_object_or_404(Reference, pk=id)
    data = object.to_dict()
    if request.user.has_perm('references.change_reference'):
        data['edit_url'] = reverse('edit_reference', args=[object.pk])
        data['edit_url'] = data['edit_url'].replace(re.search('^/\w+', data['edit_url']).group(),
                                                    "/%s" % request.user.profile.language)
        data['url'] = data['url'].replace(re.search('^/\w+', data['url']).group(),
                                          "/%s" % request.user.profile.language)

    return render_json(object=data)


@csrf_exempt
@login_or_token_required()
def approve_reference(request):
    if request.method == 'POST':
        reference = get_object_or_404(Reference, pk=request.POST['id'])
        if request.POST['is_approved'] == '1':
            reference.is_approved = True
        else:
            reference.is_approved = False
            reference.is_published = False
        reference.save()
        return render_json(reference.to_dict())
    else:
        raise Http404


@csrf_exempt
@login_or_token_required()
def publish_reference(request):
    if request.method == 'POST':
        reference = get_object_or_404(Reference, pk=request.POST['id'])
        if request.POST['is_published'] == '1':
            reference.is_published = True
        else:
            reference.is_published = False
        reference.save()
        return render_json(reference.to_dict())
    else:
        raise Http404


@csrf_exempt
def filter_values(request, id):
    values = []
    if request.method == 'POST':
        market = request.POST['market']
        if market == '':
            return render_json({'values': [v.to_dict() for v in values]})
        if id == "id_type":
            values = Type.objects.filter(pk__in=Type.objects.filter(references__market=market).order_by(get_language()))
        elif id == "id_filter_solution":
            if 'type' in request.POST:
                type = request.POST['type']
                filter = Q(references__market=market, references__type=type, references__is_approved=True)
            else:
                filter = Q(references__market=market, references__is_approved=True)

            if request.user.is_authenticated():
                values = FilterSolution.objects.filter(
                    pk__in=FilterSolution.objects.filter(filter).order_by(get_language()))
            else:
                values = FilterSolution.objects.filter(
                    pk__in=FilterSolution.objects.filter(filter, references__is_published=True).order_by(
                        get_language()))

        output = render_json({'values': [v.to_dict() for v in values]})
        return output

    else:
        raise Http404