from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db import connection
from itertools import *

# Create your views here.
def crud_index(request):
	alumnos = Alumno.objects.all()
	profesor = Profesor.objects.all()
	cursos = Curso.objects.all()
	pruebas = Prueba.objects.all()
	cursoalumnos = CursoAlumno.objects.all()
	cursopruebaalumnos = CursoPruebaAlumno.objects.all()

	return render(request, 'crud_index.html', {'alumnos': alumnos, 'profesores': profesor, 'cursos': cursos, 'pruebas':pruebas, 'cursoalumnos': cursoalumnos, 'cursopruebaalumnos': cursopruebaalumnos})

def crud_nuevoAlumno(request):
	form = AlumnoForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('crud_index')
	return render(request, 'crud_nuevoAlumno.html', {'form': form})

def crud_updateAlumno(request, rutIn):
	alumno = Alumno.objects.get(rut=rutIn)
	form = AlumnoForm(request.POST or None, instance=alumno)
	if form.is_valid():
		form.save()
		return redirect('crud_index')
	return render(request, 'crud_nuevoAlumno.html', {'form': form, 'alumnos': alumno})

def crud_deleteAlumno(request, rutIn):
	alumno = Alumno.objects.get(rut=rutIn)
	if request.method == 'POST':
		
		alumno.delete()
		return redirect('crud_index')
	return render(request, 'crud_deleteAlumnoConfirm.html', {'rutElimina': alumno})

def crud_nuevoProfesor(request):
	form = ProfesorForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('crud_index')
	return render(request, 'crud_nuevoProfesor.html', {'form': form})

def crud_updateProfesor(request, rutIn):
	profesor = Profesor.objects.get(rut=rutIn)
	form = ProfesorForm(request.POST or None, instance=profesor)
	if form.is_valid():
		form.save()
		return redirect('crud_index')
	return render(request, 'crud_nuevoProfesor.html', {'form': form, 'profesores': profesor})

def crud_deleteProfesor(request, rutIn):
	profesor = Profesor.objects.get(rut=rutIn)
	if request.method == 'POST':
		
		profesor.delete()
		return redirect('crud_index')
	return render(request, 'crud_deleteProfesorConfirm.html', {'rutElimina': profesor})	

def crud_nuevaPrueba(request):
	form = PruebaForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('crud_index')
	return render(request, 'crud_nuevaPrueba.html', {'form': form})

def crud_updatePrueba(request, idPruebaIn):
	prueba = Prueba.objects.get(idPrueba=idPruebaIn)
	form = PruebaForm(request.POST or None, instance=prueba)
	if form.is_valid():
		form.save()
		return redirect('crud_index')
	return render(request, 'crud_nuevaPrueba.html', {'form': form, 'pruebas': prueba})

def crud_deletePrueba(request, idPruebaIn):
	prueba = Prueba.objects.get(idPrueba=idPruebaIn)
	if request.method == 'POST':
		prueba.delete()
		return redirect('crud_index')
	return render(request, 'crud_deletePruebaConfirm.html', {'idPruebaElimina': prueba})

def crud_nuevoCurso(request):
	form = CursoForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('crud_index')
	return render(request, 'crud_nuevoCurso.html', {'form': form})

def crud_updateCurso(request, idCursoIn):
	curso = Curso.objects.get(idCurso=idCursoIn)
	form = PruebaForm(request.POST or None, instance=curso)
	if form.is_valid():
		form.save()
		return redirect('crud_index')
	return render(request, 'crud_nuevoCurso.html', {'form': form, 'cursos': curso})

def crud_deleteCurso(request, idCursoIn):
	curso = Curso.objects.get(idCurso=idCursoIn)
	if request.method == 'POST':
		curso.delete()
		return redirect('crud_index')
	return render(request, 'crud_deleteCursoConfirm.html', {'idCursoElimina': curso})

def crud_nuevoCursoAlumno(request):
	form = CursoAlumnoForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('crud_index')
	return render(request, 'crud_nuevoCursoAlumno.html', {'form': form})

def crud_updateCursoAlumno(request, idCAIn):
	cursoalumno = CursoAlumno.objects.get(idCA=idCAIn)
	form = PruebaForm(request.POST or None, instance=cursoalumno)
	if form.is_valid():
		form.save()
		return redirect('crud_index')
	return render(request, 'crud_nuevoCursoAlumno.html', {'form': form, 'cursoalumnos': cursoalumno})

def crud_deleteCursoAlumno(request, idCAIn):
	cursoalumno = CursoAlumno.objects.get(idCA=idCAIn)
	if request.method == 'POST':
		cursoalumno.delete()
		return redirect('crud_index')
	return render(request, 'crud_deleteCusoAlumnoConfirm.html', {'idCAElimina': cursoalumno})

def crud_nuevoCursoPruebaAlumno(request):
	form = CursoPruebaAlumnoForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('crud_index')
	return render(request, 'crud_nuevoCursoPruebaAlumno.html', {'form': form})

def crud_updateCursoPruebaAlumno(request, idCursoAlumnoAIn):
	cursopruebaalumno = CursoPruebaAlumno.objects.get(idCursoAlumno=idCursoAlumnoAIn)
	form = CursoPruebaAlumnoForm(request.POST or None, instance=cursopruebaalumno)
	if form.is_valid():
		form.save()
		return redirect('crud_index')
	return render(request, 'crud_nuevoCursoPruebaAlumno.html', {'form': form, 'cursopruebaalumnos': cursopruebaalumno})

def crud_deleteCursoPruebaAlumno(request, idCursoAlumnoAIn):
	cursopruebaalumno = CursoPruebaAlumno.objects.get(idCursoAlumno=idCursoAlumnoAIn)
	if request.method == 'POST':
		cursopruebaalumno.delete()
		return redirect('crud_index')
	return render(request, 'crud_deleteCursoPruebaAlumnoConfirm.html', {'idCursoALumnoElimina': cursopruebaalumno})

def listaPromedio(request):
	alumnos = Curso.objects.raw('''SELECT avg("crud_cursopruebaalumno"."nota") as "Promedio", "crud_alumno"."rut", "crud_alumno.nombre", "crud_alumno.apellido", "crud_curso"."nombreCurso" FROM "crud_alumno" INNER JOIN "crud_cursoalumno" on "crud_alumno"."rut" = "crud_cursoalumno"."rutAlumno" INNER JOIN "crud_cursopruebaalumno" on "crud_cursoalumno"."rutAlumno" = "crud_cursopruebaalumno"."idcursoalumno" INNER JOIN "crud_curso" on "crud_curso"."id" = "crud_cursoalumno"."idcurso" GROUP BY "crud_alumno"."rut", "crud_curso"."nombre"''')
	return render(request, 'listaPromedio.html', {'alumnos': alumnos})

def listaPromediosRojos(request):
	alumnos = Alumnos.objects.raw('''SELECT "tabPromedio"."nombreAl", "tabPromedio"."apellidoAl", "tabPromedio"."NombreCurso" FROM (SELECT avg("crud_cursopruebaalumno"."nota") "promedio", "crud_alumno"."rut" as "Rut_Estudiante", "crud_alumno"."nombre" as "nombreAl", "crud_alumno"."apellido" as "apellidoAl", "crud_curso"."nombre" as "NombreCurso" from "crud_alumno" 
		INNER JOIN "crud_cursoalumno" on "crud_alumno"."rut" = "crud_cursoalumno"."rutAlumno"
		INNER JOIN "crud_cursopruebaalumno" on "crud_cursoalumno"."rutAlumno" = "cursopruebaalumno"."idCursoAlumno"
		INNER JOIN "crud_curso" on "crud_curso"."id" = "crud_cursoalumno"."idCurso"
		GROUP BY "crud_alumno"."rut", "crud_curso"."nombre") "tabPromedio"
	GROUP BY "tabPromedio"."Rut_Estudiante"	HAVING sum(if( "tabPromedio"."promedio" <=4,1,0)) >1''')
	return render(request, 'listaPromedioRojo.html', {'alumnos': alumnos})