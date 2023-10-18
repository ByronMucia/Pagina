from django.contrib.auth.models import AbstractUser
from django.db import models



class PerfilUsuario(AbstractUser):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dpi = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128, default='valor_predeterminado')

    # No necesitas sobrescribir __init__ si no estás agregando lógica adicional a él
    # y el constructor de AbstractUser funciona bien por defecto.

    # Define related_name para evitar colisiones
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='perfil_usuarios',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='perfil_usuarios',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def set_default_password(self, password):
        # Utiliza la función de AbstractUser para establecer la contraseña
        self.set_password(password)
        self.save()

    def __str__(self):
        return self.username

