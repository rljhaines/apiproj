from django.conf.urls import patterns, include, url
from api import views

urlpatterns = patterns('',
        url(r'simpfunc/', views.simpfunc),
        url(r'otherfunc/', views.anotherfunc),
)
