from django import forms
from .models import *

class AlumnoForm(forms.ModelForm):
	class Meta:
		model = Alumno
		fields = ['rut','nombre','apellido']

class ProfesorForm(forms.ModelForm):
	class Meta:
		model = Profesor
		fields = ['rut','nombre','apellido']

class PruebaForm(forms.ModelForm):
	class Meta:
		model = Prueba
		fields = ['idPrueba', 'idCurso', 'materia']

class CursoPruebaAlumnoForm(forms.ModelForm):
	class Meta:
		model = CursoPruebaAlumno
		fields = ['idCursoAlumno', 'idPrueba', 'nota']

class CursoForm(forms.ModelForm):
	class Meta:
		model = Curso
		fields = ['idCurso', 'rutProfesor','nombreCurso']

class CursoAlumnoForm(forms.ModelForm):
	class Meta:
		model = CursoAlumno
		fields = ['idCA', 'idCurso', 'rutAlumno']