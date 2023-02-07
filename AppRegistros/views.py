from django.shortcuts import render
from django.http import HttpResponse
from AppRegistros.models import *
from AppRegistros.forms import *
# Create your views here.

def inicio(request):
     return render(request, "AppRegistro/inicio.html")

# Ver objetos 
def ver_estudiantes(request):
     
     listestudiantes= Estudiantes.objects.all()
     
     return render(request, "AppRegistro/ver_estudiantes.html", {"lista1": listestudiantes})

def ver_profesores(request):
     
     listprofes= Profesor.objects.all()
     
     return render(request, "AppRegistro/ver_profesores.html", {"lista1": listprofes})

def ver_cursos(request):
     
     listcursos= Curso.objects.all()
     return render(request, "AppRegistro/ver_cursos.html", {'lista1': listcursos})

def ver_entregas(request):
     
     listentregas= Entregas.objects.all()
     
     return render(request, "AppRegistro/ver_entregas.html", {'lista1': listentregas})

#Crear objetos

def crearEstudiantes(request):
     
     if request.method == 'POST':
          
          formulario1 = EstudiantesFormulario(request.POST)
          
          if formulario1.is_valid():
               
               infoD= formulario1.cleaned_data
               
               estudiante1= Estudiantes(nombre=infoD["nombre"], apellido= infoD['apellido'], camada= infoD['camada'], nacimiento=infoD['nacimiento'])
               
               estudiante1.save()
               
               return render(request, "AppRegistro/inicio.html")
     else:
     
          formulario1=EstudiantesFormulario()
               
          return render(request, "AppRegistro/estudianteForm.html", {"form1":formulario1 })
     
def crearProfesores(request):
     
     if request.method == 'POST':
          
          formulario1 = ProfesorFormulario(request.POST)
          
          if formulario1.is_valid():
               
               infoD= formulario1.cleaned_data
               
               profesor1= Profesor(nombre=infoD["nombre"], apellido= infoD['apellido'], email=infoD['email'], profesion= infoD['profesion'])
               
               profesor1.save()
               
               return render(request, "AppRegistro/inicio.html")
     else:
     
          formulario1=ProfesorFormulario()
               
          return render(request, "AppRegistro/profesorForm.html", {"form1":formulario1 })

def crearCursos(request):
     
     if request.method == 'POST':
          
          formulario1 = CursoFormulario(request.POST)
          
          if formulario1.is_valid():
               
               infoD= formulario1.cleaned_data
               
               curso1= Curso(nombre=infoD["nombre"], camada= infoD['camada'], curso=infoD['curso'])
               
               curso1.save()
               
               return render(request, "AppRegistro/inicio.html")
     else:
     
          formulario1=CursoFormulario()
               
          return render(request, "AppRegistro/cursoForm.html", {"form1":formulario1 })
     
def crearEntregas(request):
     
     if request.method == 'POST':
          
          formulario1 = EntregasFormulario(request.POST)
          
          if formulario1.is_valid():
               
               infoD= formulario1.cleaned_data
               
               entrega1= Entregas(nombre=infoD["nombre"],fecha= infoD['fecha'], entregado= infoD['entregado'])
               
               entrega1.save()
               
               return render(request, "AppRegistro/inicio.html")
     else:
     
          formulario1=EntregasFormulario()
               
          return render(request, "AppRegistro/entregaForm.html", {"form1":formulario1 })   
     
     
#Buscar objetos  
     
def busquedaCamada(request):
     return render(request, "AppRegistro/busquedaCamada.html")

def resultadoBusqueda(request):
     
     if request.GET['camada']:
          camada = request.GET['camada']
          cursos= Curso.objects.filter(camada__iexact=camada)
          return render(request, "AppRegistro/resultado.html", {"cursos": cursos, "camada": camada})
     
     else:
          
          respuesta= "No enviaste datos"
          
          return HttpResponse(respuesta)
