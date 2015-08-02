# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('fs_ref.app.references.views',
    url(r'^$', 'list_references', name='references'),
    url(r'^all/$', 'list_all', name='all_references'),
    url(r'^add/$', 'edit_reference', name='add_reference'),
    url(r'^(?P<id>\d+)/edit/$', 'edit_reference', name='edit_reference'),
    url(r'^(?P<id>\d+)/translate/$', 'translate_reference', name='translate_reference'),
    url(r'^(?P<id>\d+)/upload-images/$', 'upload_images', name='reference_upload_images'),
    url(r'^customers/$', 'list_customers', name='list_customers'),
    url(r'^customers/(?P<customer_id>\d+)/edit/$', 'edit_customer', name='edit_customer'),
    url(r'^customers/(?P<customer_id>\d+)/delete/$', 'delete_customer', name='delete_customer'),
    url(r'^(?P<slug>[a-z0-9-_]+)/$', 'view_reference', name='view_reference'),
)
