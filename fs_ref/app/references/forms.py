from django import forms
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.forms.util import ErrorList
from django.utils.translation import ugettext_lazy as _
from fs_ref.app.references.models import (Customer, EnglishTranslation, FilterSolution,
                                          Manufacturer, Market, Reference, Type)


class ReferenceSearchForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ('market', 'type', 'filter_solution', 'manufacturer')

    def __init__(self, show_unpublished=False, *args, **kwargs):
        super(ReferenceSearchForm, self).__init__(*args, **kwargs)

        self.fields['market'].widget.attrs['class'] = 'input-medium'
        self.fields['type'].widget.attrs['class'] = ' input-medium'
        self.fields['filter_solution'].widget.attrs['class'] = 'input-medium'
        self.fields['manufacturer'].widget.attrs['class'] = 'input-medium'

        if show_unpublished:
            filter = Q(references__is_approved=True)
        else:
            filter = Q(references__is_approved=True, references__is_published=True)

        self.fields['market'].queryset = Market.objects.filter(
            pk__in=Market.objects.filter(filter).exclude(references=None)
        )
        self.fields['manufacturer'].queryset = Manufacturer.objects.filter(
            pk__in=Manufacturer.objects.filter(filter).exclude(references=None)
        )

        if self.instance.market_id:
            self.fields['type'].queryset = Type.objects.filter(
                pk__in=Type.objects.filter(filter, references__market_id=self.instance.market_id)
            )

            if self.instance.type_id:
                self.fields['filter_solution'].queryset = FilterSolution.objects.filter(
                    pk__in=FilterSolution.objects.filter(
                        filter,
                        references__market_id=self.instance.market_id,
                        references__type_id=self.instance.type_id
                    )
                )
            else:
                self.fields['filter_solution'].choices = [('', '---------')]

        else:
            self.fields['type'].choices = [('', '---------')]


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = (
            'title',
            'market', 'type', 'filter_solution',
            'country', 'salesman', 'customer',
            'customer_contact', 'date_installed',
            'is_customer_public', 'has_borrowed_products_before_purchase',
            'application',
            'machine', 'machine_type',
            'filtering_level', 'filtering_standard',
            'fluid', 'fluid_manufacturer',
            'fluid_type', 'system_volume',
            'flow', 'flow_unit',
            'viscosity', 'viscosity_type',
            'pressure', 'temp',
            'manufacturer', 'filter', 'filter_element',
            'analysis_before', 'analysis_after',
            'cost_reductions',
            'problem',
            'solution',
        )

    def __init__(self, *args, **kwargs):
        super(ReferenceForm, self).__init__(*args, **kwargs)

        self.fields['application'].widget = forms.TextInput()
        self.fields['filter'].widget = forms.TextInput()
        self.fields['filter_element'].widget = forms.TextInput()

        self.fields['title'].widget.attrs['class'] = 'span9'
        self.fields['application'].widget.attrs['class'] = 'span9'
        self.fields['problem'].widget.attrs['class'] = 'tiny-simple span9'
        self.fields['solution'].widget.attrs['class'] = 'tiny-simple span9'

        self.fields['customer'].help_text = \
            '<a href="#customer-form-modal" data-toggle="modal" class=" btn btn-small pull-right">%s</a>' % \
            "Add a new customer"

        for field in self.fields:
            if self.fields[field].widget.__class__ == forms.Select:
                self.fields[field].widget.attrs['class'] = 'chosen'

        self.fields['date_installed'].widget.attrs['class'] = 'datepicker'
        self.fields['date_installed'].widget.attrs['placeholder'] = _('yyyy-mm-dd')

        users = [('', '---------')] + [(u.pk, "%s %s" % (u.first_name, u.last_name)) for u in User.objects.filter(is_active=True)]
        self.fields['salesman'].choices = users

    def clean(self):
        cleaned_data = super(ReferenceForm, self).clean()
        if cleaned_data['problem'] == '' and cleaned_data['solution'] == '':
            self._errors['problem'] = ErrorList([
                _('Problem <strong>or</strong> solution has to be filled')
            ])
            self._errors['solution'] = ErrorList([
                _('Problem <strong>or</strong> solution has to be filled')
            ])

        return cleaned_data


class EnglishTranslationForm(forms.ModelForm):
    class Meta:
        model = EnglishTranslation
        fields = (
            'title',

            'application',
            'machine',
            'machine_type',

            'fluid',
            'fluid_manufacturer',
            'fluid_type',
            'filtering_level',
            'cost_reductions',

            'filter',
            'filter_element',

            'analysis_before',
            'analysis_after',

            'problem',
            'solution',
        )

    def __init__(self, *args, **kwargs):
        super(EnglishTranslationForm, self).__init__(*args, **kwargs)
#
        self.fields['application'].widget = forms.TextInput()
        self.fields['filter'].widget = forms.TextInput()
        self.fields['filter_element'].widget = forms.TextInput()
#
        self.fields['title'].widget.attrs['class'] = 'span9'
        self.fields['application'].widget.attrs['class'] = 'span9'
        self.fields['analysis_before'].widget.attrs['class'] = 'span9'
        self.fields['analysis_before'].widget.attrs['rows'] = '3'
        self.fields['analysis_after'].widget.attrs['class'] = 'span9'
        self.fields['analysis_after'].widget.attrs['rows'] = '3'
        self.fields['problem'].widget.attrs['class'] = 'tiny-simple span9'
        self.fields['solution'].widget.attrs['class'] = 'tiny-simple span9'

    def clean(self):
        cleaned_data = super(EnglishTranslationForm, self).clean()
        if cleaned_data['problem'] == '' and cleaned_data['solution'] == '':
            self._errors['problem'] = ErrorList([_('Problem <strong>or</strong> solution has to be filled')])
            self._errors['solution'] = ErrorList([_('Problem <strong>or</strong> solution has to be filled')])

        return cleaned_data


class ReferenceFilesForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = (
            'illustration1', 'illustration2', 'illustration3',
            'file',
        )


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'website', 'industry', 'country')
