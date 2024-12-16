from rest_framework import serializers
from .models import Seminario, Instituciones

class SeminarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminario
        fields = ('__all__')

class InstitucionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituciones
        fields = ('__all__')