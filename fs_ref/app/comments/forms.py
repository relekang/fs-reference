# -*- coding: utf-8 -*-
from django import forms
from fs_ref.app.comments.models import ReferenceComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = ReferenceComment

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['reference'].widget = forms.HiddenInput()
        self.fields['user'].widget = forms.HiddenInput()