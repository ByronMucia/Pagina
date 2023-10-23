from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from .forms import RegistroForm  
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

class VRegistro(View):
    
    def get(self, request):
        form = RegistroForm()  # Usar tu formulario personalizado
        return render(request, "registro/registro.html", {"form": form})

    def post(self, request):
        form = RegistroForm(request.POST)  # Usar tu formulario personalizado
        if form.is_valid():
        
           usuario=form.save()
        
           login(request,usuario)
        
           return redirect('Home' )
    
        else:
            for msg in  form.error_messages:
                messages.error(request,form.error_messages[msg])
                
        return render (request,"registro/registro.html",{"form":form}) 
    
def cerrar_sesion(request):
    logout(request)
    
    return redirect('Home')    

def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request,usuario)
                return redirect('Home')
            else:
                messages.error(request, "usuario no válido")
                
        else:
            messages.error(request, "Información Incorrecta")
            
    form=AuthenticationForm()
    return render(request, "login/login.html", {"form":form})  



def Administrador(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(request=request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                admin_url = reverse('admin:index')
                return redirect(admin_url)
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información no válida")

    form = AuthenticationForm()
    return render(request, "login/loginM.html", {"form": form})