from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Curso
from .models import Orla

def curso_list(request):
    curso = Curso.objects.filter(num='1')
    return render(request,
                  'orla.html',
                  {'curso': curso})

def orla_list(request):
    return render(request, 'orla.html', {'orla': orla})
 

def home(request):
    return HttpResponse('¡Hola Mundo!')
