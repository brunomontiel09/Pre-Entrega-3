from django.contrib import admin
from AppRegistros.models import *

# Register your models here.

admin.site.register(Estudiantes)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Entregas)

