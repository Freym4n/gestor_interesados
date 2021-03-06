from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse, reverse_lazy
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .forms import LoginUserForm, clienteForm
from .models import Peticion, Cliente, Servicio
from django.http import HttpResponseRedirect
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.template import loader
from django.views import generic
from django.http import HttpResponse

# Create your views here.
from .serializers import ServicioSerializado, PeticionSerializer


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
        peticiones = Peticion.objects.filter().order_by("nombre")
        context = {'peticiones': peticiones}
        return render(request, "main/peticiones.html", context)
    else:
        return HttpResponseRedirect(reverse('auth:login'))


def clientes(request):
    if request.user.is_authenticated:
        clientes = Cliente.objects.filter()
        form = clienteForm
        servicios = Servicio.objects.filter()
        context = {'clientes': clientes, 'form':form, 'servicios':servicios}
        return render(request, 'main/inventario.html', context)
    else:
        return HttpResponseRedirect(reverse('auth:login'))



def busqueda(request):
    if request.method == 'POST':
        form_data = request.POST
        user_input = form_data['user_input']
        form = clienteForm
        servicios = Servicio.objects.filter()
        clientes = Cliente.objects.filter(nombre__contains=user_input)
        template = loader.get_template("main/inventario.html")
        context = {
            "clientes": clientes,
            "form":form,
            "servicios":servicios
        }
        return HttpResponse(template.render(context, request))
    else:
        redirect('main:inventario')

def busqueda_peticion(request):
    if request.method == 'POST':
        form_data = request.POST
        user_input = form_data['user_input']
        peticiones = Peticion.objects.filter(nombre__contains=user_input)
        template = loader.get_template("main/peticiones.html")
        context = {
            'peticiones':peticiones
        }
        return HttpResponse(template.render(context, request))
    else:
        redirect('main:home')



def agregar_cliente(request):
    if request.method == 'POST':
        form_data = request.POST
        cliente = Cliente(
            nit=form_data['nit'],
            nombre=form_data['nombre'],
            telefono=form_data['telefono'],
            servicio=Servicio.objects.get(id = form_data['servicio']),
            fecha = form_data['fecha'],
        )
        cliente.save()
        return redirect('main:clientes')

def eliminar_cliente(request, id_cliente):
    Cliente.objects.get(id = id_cliente).delete()
    return redirect('main:clientes')

def cambiar_estado(request, id_peticion):
    print('entra a la vista')
    peticion = Peticion.objects.get(id = id_peticion)
    peticion.estado_revision = (peticion.estado_revision^1)
    peticion.save()
    return redirect('main:home')


def editar_cliente(request,id_cliente):
    target = Cliente.objects.get(id = id_cliente)
    clientes = Cliente.objects.filter()
    form = clienteForm
    servicios = Servicio.objects.filter()
    context = {'clientes': clientes, 'form':form, 'servicios':servicios, 'target':target}
    return render(request, 'main/editar_cliente.html', context)
    



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


class PetitionView(APIView):

    def get(self, request):
        petitions = Peticion.objects.all().order_by('nombre')
        serializer = ServicioSerializado(petitions, many=True)
        return Response({"petitions": serializer.data})

    def post(self, request):
        petition = request.data.get('petition')
        serializer = PeticionSerializer(data=petition)
        if serializer.is_valid(raise_exception=True):
            saved_petition = serializer.save()
            return Response({"success": "Article '{}' created successfully".format(saved_petition.nombre)})
        return Response({"failure": "Article '{}' not created"})
