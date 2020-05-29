from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import path, reverse
from .forms import LoginUserForm
from .models import Servicio, Peticion, contenido_nosotros, contenido_servicio, Cliente
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.views import Response
from .serializers import ServicioSerializado


# Create your views here.

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

        context = {'form':form}
        return render(request, "main/auth/login.html",context)


def logout(request):
    do_logout(request)
    return HttpResponseRedirect(reverse('auth:login'))

def Home(request):
    return render(request, "main/peticiones.html")

