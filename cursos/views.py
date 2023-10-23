from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CursoForm
from cursos.models import Curso
from django.db import connection



@login_required
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.instructor = request.user  # Establece al usuario autenticado como instructor
            curso.save()
            return redirect('lista_cursos')  # Redirige a la lista de cursos

    else:
        form = CursoForm()

    return render(request, 'cursos/crear_curso.html', {'form': form})

def lista_cursos(request):
    cursos = Curso.objects.all()  # Obtén la lista de cursos disponibles
    context = {'cursos': cursos}
    return render(request, 'lista/lista_cursos.html', context) 
