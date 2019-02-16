
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name="aplikacija"

urlpatterns = [
    url(r'^$', views.index.as_view(), name='index'),
    url(r'prodavnica/$', views.prodza.as_view(), name='prodza'),
    url(r'prozivodi/$', views.proizvodi.as_view(), name='proizvodi'),
    url(r'narudzbina/$', views.narudzbina.as_view(), name='narudzbina'),
    url(r'prodavnica/add/$', views.NovaProdavnica.as_view(), name='prodavnica_add'),
    url(r'proizvodi/add/$', views.NoviProizvod.as_view(), name='proizvodi_add'),
    url(r'porudzbina/add/$', views.NovaPorudzbina.as_view(), name='porudzbina_add'),
    url(r'administrator/$', views.administratorView.as_view(), name='administrator'),
    url(r'(?P<pk>[0-9]+)/$', views.detailView.as_view(), name='detail'),
    url(r'search/$', views.search, name='search'),
    #url(r'^login/$', auth_views.login, name='login'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
]


