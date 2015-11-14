# -*- coding: utf-8 -*-
from django.http import Http404
from django.http.response import JsonResponse


def render_json(object=None, error=None, success=None):
    json_data = object
    if object is None:
        if error is None and success is None:
            error = 'To few arguments to render json'
            json_data = {'error': error}
        elif error is not None:
            json_data = {'error': error}
        elif success is not None:
            json_data = {'success': success}
    return JsonResponse(json_data, safe=False)


class login_or_token_required:
    """
    a api decorator that will check if user is logged in or has a token to access the data
    """

    def __call__(self, func):
        def check_permission(request, *args, **kwargs):
            u = request.user
            if u.is_authenticated():
                return func(request, *args, **kwargs)
            else:
                # Gives 404 until tokens are implemented
                raise Http404

        return check_permission
