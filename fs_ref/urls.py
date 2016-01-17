from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.http import HttpResponse
from fs_ref.app.references.feeds import RssFeed

admin.autodiscover()

# Robots
urlpatterns = [
    url(r'^robots\.txt$', lambda r: HttpResponse(
        'User-agent: *\nDisallow: /api/\nDisallow: ' +
        '/backup/\nDisallow: /accounts/\nDisallow: /admin/',
        content_type='text/plain'
    )),
]

urlpatterns += i18n_patterns(
    url(r'^api/', include('fs_ref.api.urls')),
    url(r'^admin/users/', include('fs_ref.app.users.urls')),
    url(r'^admin/', include('fs_ref.app.fs_admin.urls')),
    url(r'^references/', include('fs_ref.app.references.urls')),
    url(r'^profile/', include('fs_ref.core.profiles.urls')),
    url(r'^api/', include('fs_ref.api.urls')),
    url(r'^comments/edit/(?P<comment_id>\d+)/$', 'fs_ref.app.comments.views.edit_comment',
        name='edit_comment'),
    url(r'^comments/delete/(?P<comment_id>\d+)/$', 'fs_ref.app.comments.views.delete_comment',
        name='delete_comment'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^nadmin/', include(admin.site.urls)),
    url(r'^$', 'fs_ref.app.references.views.list_references', name='references'),
    url(r'^rss/$', RssFeed()),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        }),
    ]
