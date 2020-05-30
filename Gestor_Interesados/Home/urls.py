from django.urls import path
from django.conf.urls import url

from . import views
from .views import ServiceView, PetitionView
from .views import editar_cliente

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('main/home', views.Home, name='home'),
    path('main/clientes', views.clientes, name='clientes'),
    path('main/search',views.busqueda, name='busqueda'),
    path('main/search_petition',views.busqueda_peticion, name='busqueda_peticion'),
    path('main/agregar', views.agregar_cliente, name= 'agregar_cliente'),
    path('main/eliminar/<int:id_cliente>', views.eliminar_cliente, name= 'eliminar_cliente'),
    path('main/editar/<int:id_cliente>',views.editar_cliente,name='editar_cliente'),
    path('main/cambiar_estado/<int:id_peticion>',views.cambiar_estado, name="cambiar_estado"),
    url('services/', ServiceView.as_view()),
    url('petitions/', PetitionView.as_view()),
]
