from django.urls import path

from .views import VRegistro, cerrar_sesion, logear
from .views import VRegistro

urlpatterns = [
    
    path("",VRegistro.as_view(), name="Autenticacion"),
    
    path("cerrar_sesion",cerrar_sesion, name="cerrar_sesion"),
    
    path("logear",logear, name="logear"),
    
    path('registro/', VRegistro.as_view(), name='registro'),
    
]