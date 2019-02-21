from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.template.response import TemplateResponse
from django.views.generic import TemplateView


class LandingView(TemplateView):
    template_name = "equeue/index.html"


class LoginView(TemplateView):
    template_name = "equeue/login.html"

