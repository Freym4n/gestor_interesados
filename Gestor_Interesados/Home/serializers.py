from rest_framework import serializers
from .models import Servicio
class ServicioSerializado(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields= '__all__'