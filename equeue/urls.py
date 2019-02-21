from django.urls import path

from . import views


app_name = 'equeue'
urlpatterns = [
    path('', views.LandingView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
]