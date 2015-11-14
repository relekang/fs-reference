import re

from django.template.base import Library
from django.utils.translation import ugettext_lazy as _

register = Library()


@register.filter
def comma_list(list):
    return ', '.join([str(item) for item in list])


@register.filter
def boolean(value):
    if value is None:
        return value
    if value:
        return _('Yes')
    else:
        return _('No')


@register.filter
def excerpt(value):
    for s in re.findall('<img src=".*"[ ]+\/>', value):
        value = value.replace(s, '')
    for s in re.findall('<p>', value):
        value = value.replace(s, '')
    for s in re.findall('<\/p>', value):
        value = value.replace(s, '')
    return value[:400].strip()


@register.filter
def mod(value, arg):
    return value % arg


@register.filter
def lang_path(path, arg):
    if re.search(r'^/[a-z][a-z]/', path):
        path = path.replace(re.search(r'^/[a-z][a-z]/', path).group(), "/%s/" % arg)

    return path
