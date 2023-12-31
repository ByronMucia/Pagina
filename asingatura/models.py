from django.db import models

# Create your models here.

class CategoriaAsig(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoriaAsig"
        verbose_name_plural="categoriasAsig"

    def __str__(self):
        return self.nombre


class Asignatura(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaAsig, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="media", null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

  

    class Meta:
        verbose_name="Asignatura"
        verbose_name_plural="Asignaturas"