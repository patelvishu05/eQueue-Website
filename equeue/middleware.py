#
# class AuthRequiredMiddleware(object):
#     def process_request(self, request):
#         if not request.user.is_authenticated():
#             return HttpResponseRedirect(reverse('landing'))

from . models import *
from . models import Person
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . forms import AdminLoginForm
from django.conf import settings
import re
from django.shortcuts import redirect

EXEMPT_URLS = [re.compile(settings.LOGIN_URLS.lstrip('/'))]

if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')

        if path not in settings.PUBLIC_VIEW:
            url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)
            if request.user.is_authenticated and url_is_exempt:
                return redirect(settings.LOGIN_REDIRECT_URL)
            elif request.user.is_authenticated or url_is_exempt:
                return None
            else:
                return redirect(settings.LOGIN_URLS)







