from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .forms import LoginUserForm
from .models import Peticion, Cliente
from django.http import HttpResponseRedirect
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate


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
