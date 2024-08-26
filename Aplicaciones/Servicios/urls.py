from django.urls import path,include
from rest_framework import routers
from Aplicaciones.Servicios import views

router=routers.DefaultRouter()
router.register(r'servicios', views.ServiciosViewSet)
router.register(r'restaurante', views.RestauranteViewSet)
router.register(r'bar', views.BarViewSet)
router.register(r'zonas-humedas', views.ZonasHumedasViewSet)

urlpatterns=[
    path('',include(router.urls))
]