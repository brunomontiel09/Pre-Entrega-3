from django.urls import path
from AppRegistros.views import *



urlpatterns = [
    path('inicio/', inicio, name= "Start"),
    path('estudiantes/', ver_estudiantes, name= "Ver estudiantes"),
    path('profesores/', ver_profesores, name= "Ver profesores"),
    path('cursos/', ver_cursos, name= "Ver cursos"),
    path('entregas/', ver_entregas, name="Ver entregas"),
    
    path('crear_estudiante/', crearEstudiantes, name= "Crear Estudiante"),
    path('crear_curso/', crearCursos, name= "Crear Curso"),
    path('crear_profe/', crearProfesores, name= "Crear Profesor"),
    path('crear_entrega/', crearEntregas, name= "Crear Entrega"),
    
    path('buscarCamada/', busquedaCamada, name= "Buscar Camada"),
    path('buscarCamada2/', busquedaCamada, name= "Buscar Camada2"),
    path('resultados/', resultadoBusqueda, name= "Resultado Busqueda"),

   
    
]
