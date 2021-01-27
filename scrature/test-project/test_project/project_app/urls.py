from django.contrib import admin
from django.urls import path,include ,re_path
from django.conf.urls import url
from .import views
urlpatterns = [
    path('api_view', views.api_view,name="api_view"),
    re_path(r'^api/students/$', views.students_list),
    re_path(r'^api/students/([0-9])$', views.students_detail),
]
