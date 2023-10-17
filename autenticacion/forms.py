from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import PerfilUsuario

class RegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=30, required=True, help_text="Requerido. Ingrese su nombre.")
    apellido = forms.CharField(max_length=30, required=True, help_text="Requerido. Ingrese su apellido.")
    dpi = forms.CharField(max_length=20, required=True, help_text="Requerido. Ingrese su número de DPI.")
    fecha_nacimiento = forms.DateField(required=True, help_text="Requerido. Ingrese su fecha de nacimiento (AAAA-MM-DD).")
    telefono = forms.CharField(max_length=15, required=True, help_text="Requerido. Ingrese su número de teléfono.")
    email = forms.EmailField(max_length=254, required=True, help_text="Requerido. Ingrese su dirección de correo electrónico. Debe ser única.")
    username = forms.CharField(max_length=30, required=True, help_text="Requerido. Ingrese un nombre de usuario único.")
    
    class Meta:
        model = PerfilUsuario  # Asegúrate de importar 'User' desde 'django.contrib.auth.models'
        fields = UserCreationForm.Meta.fields + ('nombre', 'apellido', 'dpi', 'fecha_nacimiento', 'telefono', 'email', 'username',)
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.nombre = self.cleaned_data['nombre']
        user.apellido = self.cleaned_data['apellido']
        user.dpi = self.cleaned_data['dpi']
        user.fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        user.telefono = self.cleaned_data['telefono']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user