from django.urls import path
from .import views 

urlpatterns = [
    path('crear_curso/', views.crear_curso, name='crear_curso'),
    path('lista_cursos/', views.lista_cursos, name='lista_cursos'),
    
    # Otras rutas de la aplicación de cursos
]
