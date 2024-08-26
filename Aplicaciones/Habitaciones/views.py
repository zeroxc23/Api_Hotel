from rest_framework import viewsets
from .serializer import HabitacionesSerializer,TipoHabitacionesSerializer
from .models import Habitaciones,TipoHabitaciones

class HabitacionesViewSet(viewsets.ModelViewSet):
    queryset=Habitaciones.objects.all()
    serializer_class=HabitacionesSerializer

class TipoHabitacionesViewSet(viewsets.ModelViewSet):
    queryset=TipoHabitaciones.objects.all()
    serializer_class=TipoHabitacionesSerializer
