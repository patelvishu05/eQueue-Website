from django.shortcuts import render
from . models import *
from django.views.generic import *
# Create your views here.
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from django.contrib.auth import *
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from . forms import KioskSignIn
from . models import Person
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . forms import AdminLoginForm


class LandingView(TemplateView):
    template_name = "equeue/index.html"


class LoginView(TemplateView):
    template_name = "equeue/login.html"


class PageNotFound(TemplateView):
    template_name = "equeue/404.html"


def createKioskView(request):
    form = KioskSignIn()
    if request.method == 'POST':
        form = KioskSignIn(request.POST)
        if form.is_valid():
            print(form.save())

    context = {
        "form": form
    }
    return render(request, "equeue/kiosk.html", context)


class PreProcess(TemplateView):

    template_name = "equeue/pre_process.html"

    def get(self, request):
        queryset = Person.objects.all()

        args = {'queryset': queryset}
        return render(request, self.template_name, args)


# @method_decorator(login_required, name='dispatch')
class AdminKioskView(TemplateView):

    template_name = "equeue/admin_kiosk.html"

    def get(self, request):
        time = 0
        i = 0

        for p in Person.objects.all():
            if i==0:
                time = p.service
            else:
                p.waitTime = p.waitTime - time
            p.lineNumber-=1
            p.save()
            i+=1

        Person.objects.get(lineNumber=0).delete()
        queryset = Person.objects.all()

        args = {'queryset': queryset}
        return render(request, self.template_name, args)


class KioskListView(ListView):
    template_name = "equeue/student-view.html"

    def get(self, request):
        queryset = Person.objects.all()
        args = {'queryset': queryset}

        return render(request, self.template_name, args)


def adminLogin(request):
    next = request.GET.get('next')
    form = AdminLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/equeue/admin-kiosk')

    context = {
        'form': form,
    }
    return render(request, "equeue/login.html", context)

