from django.urls import path
from django.conf.urls import url

from . import views
from django.urls import path
from . import views

# urlpatterns = [
#     # path('', views.index, name='index'),
#     path('',views.AboutPageView.as_view()),
#     path('date/',views.DatePageView.as_view()),
# ]
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]