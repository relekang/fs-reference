# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('fs_ref.api.views.references',
    url(r'^references/$', 'list_references', name='api.list_references'),
    url(r'^references/(?P<id>\d+)/$', 'fetch_reference', name='api.fetch_reference'),
    url(r'^references/add/$', 'add_references', name='api.add_references'),
    url(r'^references/approve/$', 'approve_reference', name='api.approve_reference'),
    url(r'^references/publish/$', 'publish_reference', name='api.publish_reference'),
    url(r'^references/filter-values/(?P<id>[a-z_-]+)/$', 'filter_values', name='api.filter_values'),
)

urlpatterns += patterns('fs_ref.api.views.comments',
    url(r'^comments/$', 'list_comments', name='api.list_comments'),
    url(r'^comments/(?P<id>\d+)/$', 'fetch_comment', name='api.fetch_comment'),
    url(r'^comments/add/$', 'add_comment', name='api.add_comment'),
    url(r'^comments/edit/(?P<comment_id>\d+)/$', 'edit_comment', name='api.edit_comment'),
)

urlpatterns += patterns('fs_ref.api.views.customers',
    url(r'^customers/add/$', 'add_customer', name='api.add_customer'),
)
