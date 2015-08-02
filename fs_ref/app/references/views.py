# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext_lazy as _

from fs_ref.app.references.models import Reference, EnglishTranslation, Customer
from fs_ref.app.references.forms import ReferenceForm, ReferenceSearchForm
from fs_ref.app.references.forms import ReferenceFilesForm, CustomerForm
from fs_ref.app.references.forms import EnglishTranslationForm


def list_references(request):
    instance = None
    if 'm' in request.GET or 't' in request.GET or 'fs' in request.GET:
        instance = Reference(
            market_id=request.GET.get('m'),
            type_id=request.GET.get('t'),
            filter_solution_id=request.GET.get('fs'),
        )
    form = ReferenceSearchForm(instance=instance)

    references = list(Reference.objects.filter(is_approved=True, is_published=True).select_related(
        'market',
        'type',
        'filter_solution',
        'manufacturer'
    ))

    if request.user.is_authenticated():
        references += list(Reference.objects.filter(is_approved=True, is_published=False)
                                            .select_related('market', 'type', 'filter_solution',
                                                            'manufacturer'))

    return render(request, 'references/base.html', locals())


def list_all(request):
    references = list(Reference.objects.filter(is_approved=True, is_published=True).select_related(
        'market',
        'type',
        'filter_solution',
        'manufacturer'
    ))

    if request.user.is_authenticated():
        references += list(Reference.objects.filter(is_approved=True,
                                                    is_published=False).select_related(
            'market',
            'type',
            'filter_solution',
            'manufacturer'
        ))
        if request.user.has_perm('references.approve_reference'):
            references += list(Reference.objects.filter(is_approved=False).select_related(
                'market',
                'type',
                'filter_solution',
                'manufacturer'
            ))

    return render(request, 'references/admin/list.html', locals())


def view_reference(request, slug):
    reference = get_object_or_404(Reference, slug=slug)

    if not request.user.is_authenticated() and not reference.is_published:
        return redirect('login')

    if not reference.is_approved and not request.user.has_perm('references.change_reference'):
        messages.warning(request, _('You do not have permission to view the reference you '
                                    'requested'))
        return redirect('references')

    return render(request, 'references/view.html', locals())


@permission_required('references.change_reference')
def edit_reference(request, id=None):
    form = ReferenceForm()
    customer_form = CustomerForm()
    if id is not None:
        reference = get_object_or_404(Reference, pk=id)
        form = ReferenceForm(instance=reference)

    if request.method == 'POST':
        form = ReferenceForm(request.POST)
        if id is not None:
            form = ReferenceForm(request.POST, instance=reference)

        if form.is_valid():
            reference = form.save()
            return redirect(reverse('view_reference', args=[reference.slug]))

    tiny_mce = True
    return render(request, 'references/edit.html', locals())


@permission_required('references.change_reference')
def upload_images(request, id):
    reference = get_object_or_404(Reference, pk=id)
    form = ReferenceFilesForm(instance=reference)
    if request.method == 'POST':
        form = ReferenceFilesForm(request.POST, request.FILES, instance=reference)
        if form.is_valid():
            form.save()
            messages.success(request, _('The files was uploaded'))
            return redirect('view_reference', reference.slug)

    return render(request, 'references/upload_images.html', locals())


@permission_required('references.change_reference')
def translate_reference(request, id):
    reference = get_object_or_404(Reference, pk=id)
    try:
        translation = reference.englishtranslation
    except EnglishTranslation.DoesNotExist:
        translation = EnglishTranslation(reference=reference)

    form = EnglishTranslationForm(instance=translation)

    if request.method == 'POST':
        form = EnglishTranslationForm(request.POST, instance=translation)
        if form.is_valid():
            form.save()
            return redirect('view_reference', reference.slug)

    tiny_mce = True
    return render(request, 'references/translate_reference.html', locals())


@permission_required('references.change_customer')
def list_customers(request):
    return render(request, 'references/admin/list_customers.html', {
        'customers': Customer.objects.all()
    })


@permission_required('references.change_customer')
def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return redirect('list_customers')

    return render(request, 'references/admin/edit_customer.html', {
        'customer': customer,
        'form': form
    })


@permission_required('references.delete_customer')
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        if request.POST.get('confirmed') == 'yes':
            customer.delete()
            messages.success(request, 'The customer was successfully deleted')
            return redirect('list_customers')

    return render(request, 'references/admin/delete_customer.html', {
        'customer': customer,
    })
