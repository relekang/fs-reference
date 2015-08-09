# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.forms.models import modelformset_factory
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from fs_ref.app.references.models import Market, Type, FilterSolution, Manufacturer
from fs_ref.app.fs_admin.forms import MarketForm, TypeForm, FilterSolutionForm, ManufacturerForm


@permission_required('references.change_market')
def edit_markets(request):
    title = _('Edit market list')
    can_add_extra = request.user.has_perm('references.add_market')

    MarketFormset = modelformset_factory(model=Market, form=MarketForm, extra=0)
    formset = MarketFormset(queryset=Market.objects.all())
    if request.method == 'POST':
        formset = MarketFormset(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, _('Markets was saved'))
    return render(request, 'admin/edit_filteringitems.html', locals())


@permission_required('references.change_type')
def edit_types(request):
    title = _('Edit application list')
    can_add_extra = request.user.has_perm('references.add_type')

    TypeFormset = modelformset_factory(model=Type, form=TypeForm, extra=0)
    formset = TypeFormset(queryset=Type.objects.all())
    if request.method == 'POST':
        formset = TypeFormset(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, _('Types was saved'))
    return render(request, 'admin/edit_filteringitems.html', locals())


@permission_required('references.change_filter_solution')
def edit_filter_solutions(request):
    title = _('Edit filter solutions list')
    can_add_extra = request.user.has_perm('references.add_filter_solution')

    FilterSolutionFormset = modelformset_factory(model=FilterSolution, form=FilterSolutionForm, extra=0)
    formset = FilterSolutionFormset(queryset=FilterSolution.objects.all())
    if request.method == 'POST':
        formset = FilterSolutionFormset(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, _('Filter solutions was saved'))
    return render(request, 'admin/edit_filteringitems.html', locals())


@permission_required('references.change_filter_solution')
def edit_manufacturers(request):
    title = _('Edit filter solutions list')
    can_add_extra = request.user.has_perm('references.add_manufacturer')

    ManufacturerFormset = modelformset_factory(model=Manufacturer, form=ManufacturerForm, extra=0)
    formset = ManufacturerFormset(queryset=Manufacturer.objects.all())
    if request.method == 'POST':
        formset = ManufacturerFormset(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, _('Filter solutions was saved'))
    return render(request, 'admin/edit_filteringitems.html', locals())
