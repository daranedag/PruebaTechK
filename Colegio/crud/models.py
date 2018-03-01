from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.
class Profesor(models.Model):
	rut = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=25)
	apellido = models.CharField(max_length=25)

	def __str__(self):
		return str(self.rut)
	
	def getNombreCompleto(self):
		return self.nombre + self.apellido

class Alumno(models.Model):
	rut = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=25)
	apellido = models.CharField(max_length=25)
	
	def __str__(self):
		return str(self.rut)

class Curso(models.Model):
	idCurso = models.IntegerField(primary_key=True)
	rutProfesor = models.ForeignKey(Profesor, on_delete = models.DO_NOTHING)
	nombreCurso = models.CharField(max_length=50)

	def __str__(self):
		return str(self.idCurso)

class Prueba(models.Model):
	idPrueba = models.IntegerField(primary_key=True)
	idCurso = models.ForeignKey(Curso, on_delete = models.DO_NOTHING)
	materia = models.CharField(max_length=25)

	def __str__(self):
		return str(self.materia)

class CursoAlumno(models.Model):
	idCA = models.IntegerField(primary_key=True)
	idCurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	rutAlumno = models.ForeignKey(Alumno,  on_delete = models.CASCADE)
	def __str__(self):
		salida = str(self.idCA)
		return str(salida)

class CursoPruebaAlumno(models.Model):
	idCursoAlumno = models.ForeignKey(CursoAlumno, on_delete=models.DO_NOTHING)
	idPrueba = models.ForeignKey(Prueba, on_delete = models.DO_NOTHING)
	nota = models.FloatField()

	def __str__(self):
		salida = str(self.idCursoAlumno)
		return str(salida)