from django.core.urlresolvers import reverse
from django.template.base import Library
from django.utils.translation import ugettext_lazy as _

register = Library()


@register.inclusion_tag('templatetags/menu.html')
def menu():
    menu = [
        {'title': _('Topics'), 'url': reverse('admin_topics')},
        {'title': _('Users'), 'url': reverse('admin_users')},
        #        {'title': _('User groups'), 'url': reverse('help_admin.views.user_groups.landing_page')},
        {'title': 'Django admin', 'url': '/admin/'},
    ]
    return {'menu': menu}
