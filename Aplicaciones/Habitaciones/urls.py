from django.urls import path,include
from rest_framework import routers
from Aplicaciones.Habitaciones import views

router=routers.DefaultRouter()
router.register(r'habitaciones',views.HabitacionesViewSet)

urlpatterns=[
    path('',include(router.urls))
]