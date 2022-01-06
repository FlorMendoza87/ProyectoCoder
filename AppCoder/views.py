from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso




# Create your views here.
def curso (self):
    curso = Curso (nombre = "Desarrollo  web", camada = "19881")
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre} Camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)

def inicio(self):
    return HttpResponse ("vista inicio")

def cursos(self):
    return HttpResponse ("vista cursos")    

def profesores(self):
    return HttpResponse ("vista profesores")

def estudiantes(self):
    return HttpResponse ("vista estudiantes")

def entregables(self):
    return HttpResponse ("vista entregables")