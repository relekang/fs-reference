# -*- coding: utf-8 -*-
import re
from django.conf import settings
from django.shortcuts import redirect
from django.utils import translation
from django.utils.translation import check_for_language


def delete_meta_language(request):
    """
    Removes HTTP_ACCEPT_LANGUAGE from request meta-info
    :param request:
    """

    if request.META.has_key('HTTP_ACCEPT_LANGUAGE'):
        del request.META['HTTP_ACCEPT_LANGUAGE']


class LanguageMiddleware:
    def process_request(self, request):
        lang_code = None
        host = request.META.get('HTTP_HOST').replace('ref.', '')

        if not settings.DEBUG:
            if host in settings.LANGUAGES_FOR_DOMAIN:
                lang_code = settings.LANGUAGES_FOR_DOMAIN[host]

        s = re.search(r'^/([a-z]{2})/', request.path)
        if s:
            path_code = s.group(1)
            if path_code == 'nb': path_code = 'no'

            if lang_code and path_code != lang_code and path_code != 'en':
                return redirect(request.path.replace(re.search('^/([a-z]{2})/', request.path).group(1), lang_code))

            # If no redirect hit before this path_code is the correct lang code
            if lang_code is None or path_code == 'en': lang_code = path_code

        elif lang_code:
            return redirect('/%s%s' % (lang_code, request.path))

        if lang_code:
            delete_meta_language(request)

            translation.activate(lang_code)
            request.LANGUAGE_CODE = lang_code