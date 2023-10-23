from django.shortcuts import render, HttpResponse
from .models import Asignatura

def blog(request):
    
    asignaturas=Asignatura.objects.all()
    
    return render(request,"blog/blog.html",{"asignaturas":asignaturas})