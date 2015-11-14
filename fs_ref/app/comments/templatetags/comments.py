# -*- coding: utf-8 -*-
from django.template.base import Library
from fs_ref.app.comments.forms import CommentForm
from fs_ref.app.comments.models import ReferenceComment

register = Library()


@register.inclusion_tag('comments/templatetags/form.html', takes_context=True)
def comment_form(context, reference):
    instance = ReferenceComment(reference=reference, user=context['user'])
    form = CommentForm(instance=instance)
    return {
        'form': form
    }


@register.inclusion_tag('comments/templatetags/list.html', takes_context=True)
def load_comments(context, reference):
    return {
        'comments': reference.comments.all().select_related('user').order_by('-timestamp'),
        'user': context['user']
    }
