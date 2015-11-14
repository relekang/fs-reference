from django.conf.urls import patterns, url

urlpatterns = patterns('fs_ref.core.profiles.views',
    url(r'^edit$', 'edit_profile', name='edit_profile'),
)
