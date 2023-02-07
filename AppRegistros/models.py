from django.db import models

# Create your models here.
class Estudiantes(models.Model):
    
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    camada= models.IntegerField()
    nacimiento= models.DateField()
    
class Profesor(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField(max_length=40)
    profesion= models.CharField(max_length=35)

class Entregas(models.Model):
    nombre= models.CharField(max_length=40)
    fecha= models.DateField()
    entregado= models.BooleanField()

class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    camada= models.IntegerField()
    curso=models.IntegerField()