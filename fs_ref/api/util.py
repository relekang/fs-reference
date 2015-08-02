# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse, Http404


def render_json(object=None, error=None, success=None):
    if object is None:
        if error is None and success is None:
            error = 'To few arguments to render json'
            json_data = json.dumps({'error': error})
        elif error is not None:
            json_data = json.dumps({'error': error})
        elif success is not None:
            json_data = json.dumps({'success': success})

    else:
        json_data = json.dumps(object)
    return HttpResponse(json_data, mimetype="application/json")


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
                #Gives 404 until tokens are implemented
                raise Http404

        return check_permission