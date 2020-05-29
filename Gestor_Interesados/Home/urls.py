from django.urls import path
from django.conf.urls import url

from . import views
from .views import ServiceView

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('main/home', views.Home, name='home'),
    path('main/clientes', views.clientes, name='clientes'),
    url('services/', ServiceView.as_view())
]
