from django.urls import path

from . import views


app_name = 'equeue'
urlpatterns = [
    path('', views.LandingView.as_view(), name='index'),
    path('login/', views.adminLogin, name='login'),
    path('kiosk/', views.createKioskView, name='kiosk'),
    path('admin-kiosk/', views.AdminKioskView.as_view(), name='admin-kiosk'),
    path('student-view/', views.KioskListView.as_view(), name="student-view")
]
