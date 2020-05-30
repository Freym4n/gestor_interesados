from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Cliente
class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
        labels = {
            'username':'Usuario',
            'password':'Contraseña'
        }
    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = self.fields['username'].label or 'Usuario'
        self.fields['password'].widget.attrs['placeholder'] = self.fields['password'].label or 'Contraseña'


class clienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields =['nit','nombre','telefono']
        labels ={'nit':'','nombre':'','telefono':''}
    def __init__(self, *args, **kwargs):
        super(clienteForm, self).__init__(*args, **kwargs)
        self.fields['nit'].widget.attrs['placeholder'] = self.fields['nit'].label or 'Nit'
        self.fields['nombre'].widget.attrs['placeholder'] = self.fields['nombre'].label or 'Nombre'
        self.fields['telefono'].widget.attrs['placeholder'] = self.fields['telefono'].label or 'Teléfono'
        
        

