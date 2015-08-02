# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from fs_ref.app.comments.forms import CommentForm
from fs_ref.app.comments.models import ReferenceComment
from fs_ref.api.util import render_json, login_or_token_required


@login_or_token_required()
def list_comments(request, ref_id):
    data_list = [item.to_dict() for item in ReferenceComment.objects.filter(reference_id=ref_id)]

    return render_json(object=data_list)


@login_or_token_required()
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return render_json({'comment': comment.to_dict()})
        else:
            return render_json(error=[{'field': k, 'error': unicode(v[0])} for k, v in form.errors.items()])


@login_or_token_required()
def edit_comment(request, comment_id):
    comment = ReferenceComment.objects.get(pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return render_json({'comment': comment.to_dict()})
        else:
            return render_json(error=[{'field': k, 'error': unicode(v[0])} for k, v in form.errors.items()])


@login_or_token_required()
def fetch_comment(request, id):
    object = get_object_or_404(ReferenceComment, pk=id)
    data = object.to_dict()

    return render_json(object=data)