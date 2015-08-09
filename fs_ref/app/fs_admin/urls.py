# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('fs_ref.app.fs_admin.views',
    url(r'^markets/$', 'edit_markets', name='markets'),
    url(r'^markets/edit$', 'edit_markets', name='edit_markets'),
    url(r'^types/$', 'edit_types', name='types'),
    url(r'^types/edit/$', 'edit_types', name='edit_types'),
    url(r'^filter-solutions/$', 'edit_filter_solutions', name='filter_solutions'),
    url(r'^filter-solutions/edit/$', 'edit_filter_solutions', name='edit_filter_solutions'),
    url(r'^manufacturers/$', 'edit_manufacturers', name='manufacturers'),
    url(r'^manufacturers/edit/$', 'edit_manufacturers', name='edit_manufacturers'),
)
