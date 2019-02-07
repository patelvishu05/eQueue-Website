from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('',views.AboutPageView.as_view()),
    path('date/',views.DatePageView.as_view()),
]