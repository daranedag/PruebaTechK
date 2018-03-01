from django.db import models

# Create your models here.
class Profesor(models.Model):
	rut = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=25)
	apellido = models.CharField(max_length=25)

class Alumno(models.Model):
	rut = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=25)
	apellido = models.CharField(max_length=25)

class Curso(models.Model):
	idCurso = models.IntegerField(primary_key=True)
	rutProfesor = models.ForeignKey(Profesor, on_delete = models.DO_NOTHING)
	nombreCurso = models.CharField(max_length=50)

class Prueba(models.Model):
	idPrueba = models.IntegerField(primary_key=True)
	idCurso = models.ForeignKey(Curso, on_delete = models.DO_NOTHING)
	materia = models.CharField(max_length=25)

class CursoAlumno(models.Model):
	idCA = models.IntegerField(primary_key=True)
	idCurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	rutAlumno = models.ForeignKey(Alumno,  on_delete = models.CASCADE)

class CursoPruebaAlumno(models.Model):
	idCursoAlumno = models.ForeignKey(CursoAlumno, on_delete=models.DO_NOTHING)
	idPrueba = models.ForeignKey(Prueba, on_delete = models.DO_NOTHING)
	nota = models.FloatField()