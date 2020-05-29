from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import LoginUserForm
from .models import Peticion, Cliente, Servicio
from django.http import HttpResponseRedirect
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate

# Create your views here.
from .serializers import ServicioSerializado


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:home'))
    else:
        form = LoginUserForm()
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    do_login(request, user)
                    return HttpResponseRedirect(reverse('main:home'))

        context = {'form': form}
        return render(request, "main/auth/login.html", context)


def logout(request):
    do_logout(request)
    return HttpResponseRedirect(reverse('auth:login'))


def Home(request):
    if request.user.is_authenticated:
        peticiones = Peticion.objects.filter()
        context = {'peticiones': peticiones}
        return render(request, "main/peticiones.html", context)
    else:
        return HttpResponseRedirect(reverse('auth:login'))


def clientes(request):
    if request.user.is_authenticated:
        clientes = Cliente.objects.filter()
        context = {'clientes': clientes}
        return render(request, 'main/inventario.html', context)
    else:
        return HttpResponseRedirect(reverse('auth:login'))


class ServiceView(APIView):

    def get(self, request):
        services = Servicio.objects.all().order_by('nombre')
        serializer = ServicioSerializado(services, many=True)
        return Response({"services": serializer.data})

    def post(self, request):
        service = request.data.get('service')
        serializer = ServicioSerializado(data=service)
        if serializer.is_valid(raise_exception=True):
            saved_service = serializer.save()
            return Response({"success": "Article '{}' created successfully".format(saved_service.nombre)})
        return Response({"failure": "Article '{}' not created"})
