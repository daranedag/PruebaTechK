from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Prueba)
admin.site.register(CursoAlumno)
admin.site.register(CursoPruebaAlumno)

