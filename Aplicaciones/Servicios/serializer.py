from rest_framework import serializers
from .models import Servicios, Restaurante, Bar, ZonasHumedas

class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = '__all__'

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'

class BarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bar
        fields = '__all__'

class ZonasHumedasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZonasHumedas
        fields = '__all__'
