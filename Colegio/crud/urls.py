from django.urls import path 
from .views import *

urlpatterns = [
	path('', crud_index, name='crud_index'),
	path('nuevoAlumno', crud_nuevoAlumno, name='crud_nuevoAlumno'),
	path('updateAlumno/<int:rutIn>/', crud_updateAlumno, name='crud_updateAlumno'),
	path('deleteAlumno/<int:rutIn>/', crud_deleteAlumno, name='crud_deleteAlumno'),

	path('nuevoProfesor', crud_nuevoProfesor, name='crud_nuevoProfesor'),
	path('updateProfesor/<int:rutIn>/', crud_updateProfesor, name='crud_updateProfesor'),
	path('deleteProfesor/<int:rutIn>/', crud_deleteProfesor, name='crud_deleteProfesor'),
	
	path('nuevaPrueba', crud_nuevaPrueba, name='crud_nuevaPrueba'),
	path('updatePrueba/<int:idPruebaIn>/', crud_updatePrueba, name='crud_updatePrueba'),
	path('deletePrueba/<int:idPruebaIn>/', crud_deletePrueba, name='crud_deletePrueba'),

	path('nuevoCurso', crud_nuevoCurso, name='crud_nuevoCurso'),
	path('updateCurso/<int:idCursoIn>/', crud_updateCurso, name='crud_updateCurso'),
	path('deleteCurso/<int:idCursoIn>/', crud_deleteCurso, name='crud_deleteCurso'),

	path('nuevoCursoAlumno', crud_nuevoCursoAlumno, name='crud_nuevoCursoAlumno'),
	path('updateCursoAlumno/<int:idCAIn>/', crud_updateCursoAlumno, name='crud_updateCursoAlumno'),
	path('deleteCursoAlumno/<int:idCAIn>/', crud_deleteCursoAlumno, name='crud_deleteCursoAlumno'),

	path('nuevoCursoPruebaAlumno', crud_nuevoCursoPruebaAlumno, name='crud_nuevoCursoPruebaAlumno'),
	path('updateCursoPruebaAlumno/<int:idCursoAlumnoAIn>/', crud_updateCursoPruebaAlumno, name='crud_updateCursoPruebaAlumno'),
	path('deleteCursoPruebaAlumno/<int:idCursoAlumnoAIn>/', crud_deleteCursoPruebaAlumno, name='crud_deleteCursoPruebaAlumno'),		

	path('listarAlumnosPromedio', listaPromedio, name='listaPromedio'),
	path('listarPromedioRojo', listaPromediosRojos, name='listaPromediosRojos'),
]