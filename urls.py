from django.urls import path, include
from . import views
from django.urls import re_path

app_name = 'polls'
urlpatterns = [
    re_path(
r'^blog/(?P<year>[0-9]{4} )/(?P<month>[0-9]{2} )/(?P<slug>[\w-]+)/$'
,views.blog_detail),

    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')

]