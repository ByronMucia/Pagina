from django.db import models
from autenticacion.models import PerfilUsuario  # Ajusta esto para importar tu modelo de usuario personalizado

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    instructor = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(PerfilUsuario, related_name='cursos_inscritos')

    def __str__(self):
        return self.titulo
    

