from django.urls import path, URLPattern, URLResolver
from django.conf.urls import url, include
from . import views


urlpatterns = [
    path('',views.login,name='login'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('main/home',views.Home,name='home'),
    path('main/clientes',views.clientes,name='clientes')
]