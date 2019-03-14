from django.shortcuts import render
from . models import *

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from . forms import KioskSignIn


class LandingView(TemplateView):
    template_name = "equeue/index.html"


class LoginView(TemplateView):
    template_name = "equeue/login.html"


def createKioskView(request):
    form = KioskSignIn()
    if request.method == 'POST':
        form = KioskSignIn(request.POST)
        # print(request.POST)
        if form.is_valid():
            print(form.save())

    context = {
        "form": form
    }
    return render(request, "equeue/kiosk.html", context)


