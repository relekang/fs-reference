from django import forms
from django.utils import translation
from fs_ref.app.references.models import Market, Type, FilterSolution, Manufacturer


class FilteringItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FilteringItemForm, self).__init__(*args, **kwargs)

        if not translation.get_language() == 'en':
            self.fields['en'].widget.attrs['readonly'] = True
        if translation.get_language() == 'no':
            self.fields['dk'].widget.attrs['readonly'] = True
            self.fields['sv'].widget.attrs['readonly'] = True
        elif translation.get_language() == 'dk':
            self.fields['no'].widget.attrs['readonly'] = True
            self.fields['sv'].widget.attrs['readonly'] = True
        elif translation.get_language() == 'sv':
            self.fields['no'].widget.attrs['readonly'] = True
            self.fields['dk'].widget.attrs['readonly'] = True


class MarketForm(FilteringItemForm):
    class Meta:
        model = Market
        fields = ('en', 'no', 'dk', 'sv')


class TypeForm(FilteringItemForm):
    class Meta:
        model = Type
        fields = ('en', 'no', 'dk', 'sv')


class FilterSolutionForm(FilteringItemForm):
    class Meta:
        model = FilterSolution
        fields = ('en', 'no', 'dk', 'sv')


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ('name', 'code')
