from django.urls import re_path
from . import views

app_name = 'myapp'
urlpatterns = [
    re_path(r'^mypath/$', views.MyView.as_view(), name='myview'),
    re_path(r'^create/$', views.MyView.as_view(), name='mycreateview'),
    re_path(r'^(?P<pk>[0-9]+)/update/$', views.MyUpdateView.as_view(), name='myupdateview'),
]
