from rest_framework import viewsets
from .models import Servicios,Restaurante,Bar,ZonasHumedas
from .serializer import ServiciosSerializer,RestauranteSerializer,BarSerializer,ZonasHumedasSerializer

class ServiciosViewSet(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializer

class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class BarViewSet(viewsets.ModelViewSet):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer

class ZonasHumedasViewSet(viewsets.ModelViewSet):
    queryset = ZonasHumedas.objects.all()
    serializer_class = ZonasHumedasSerializer