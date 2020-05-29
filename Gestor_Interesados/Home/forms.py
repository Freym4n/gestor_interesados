from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.contrib.auth.models import User

class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
        labels = {
            'username':'Usuario',
            'password':'Contraseña'
        }