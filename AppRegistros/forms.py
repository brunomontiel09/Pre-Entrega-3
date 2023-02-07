from django import forms

class EstudiantesFormulario(forms.Form):
    
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    camada= forms.IntegerField()
    nacimiento= forms.DateField()
    
class ProfesorFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=35)

class EntregasFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    fecha= forms.DateField()
    entregado= forms.BooleanField()
    
class CursoFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    camada= forms.IntegerField()
    curso=forms.IntegerField()