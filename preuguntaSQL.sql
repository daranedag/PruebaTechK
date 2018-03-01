-- 1. Escriba una Query que entregue la lista de  alumnos para el curso "programación"

SELECT DISTINCT a.rut, a.nombre, a.apellido FROM Alumno a 
	INNER JOIN CursoAlumno ca ON ca.rutAlumno = a.rut 
	INNER JOIN Curso c ON c.id = ca.idCurso 
	WHERE c.nombre IN("Programacion")

-- 2. Escriba una Query  que calcule el promedio de notas de un alumno en un curso.

SELECT AVG(CursoPruebaAlumno.nota) FROM CursoPruebaAlumno 
	INNER JOIN CursoAlumno on CursoAlumno.rutAlumno = CursoPruebaAlumno.idCursoAlumno 
	INNER JOIN Curso on Curso.id = CursoAlumno.idCA 
	INNER JOIN Alumno on Alumno.rut = CursoAlumno.rutAlumno 
	WHERE Curso.id = 1 and Alumno.rut=24086961;

-- 3. Escriba una Query que entregue a los alumnos y el promedio que tiene en cada curso.

SELECT AVG(CursoPruebaAlumno.nota) as ´Promedio´, Alumno.rut, Alumno.nombre, Alumno.apellido, Curso.nombre FROM Alumno 
	INNER JOIN CursoAlumno on Alumno.rut = CursoAlumno.rutAlumno 
	INNER JOIN CursoPruebaAlumno on CursoAlumno.rutAlumno = CursoPruebaAlumno.idCursoAlumno 
	INNER JOIN Curso on Curso.id = CursoAlumno.idCurso 
	GROUP BY Alumno.rut, Curso.nombre;

-- 4. Escriba una Query que lista a todos los alumnos con más de un curso con promedio rojo.

select  tabPromedio.nombreAl, tabPromedio.apellidoAl, tabPromedio.NombreCurso 
	from (SELECT AVG(CursoPruebaAlumno.nota) promedio, Alumno.rut as Rut_Estudiante, Alumno.nombre as nombreAl, Alumno.apellido as apellidoAl, Curso.nombre as NombreCurso from Alumno 
		INNER JOIN CursoAlumno on Alumno.rut = CursoAlumno.rutAlumno 
		INNER JOIN CursoPruebaAlumno on CursoAlumno.rutAlumno = CursoPruebaAlumno.idCursoAlumno 
		INNER JOIN Curso on Curso.id = CursoAlumno.idCurso 
		GROUP BY Alumno.rut, Curso.nombre) tabPromedio 
	GROUP BY tabPromedio.Rut_Estudiante 
	HAVING sum(if( tabPromedio.promedio <=4,1,0)) >1


-- 5. Dejando de lado el problema del cólegio se tiene una tabla con información de jugadores de tenis:

/*`PLAYERS(Nombre, Pais, Ranking)`. Suponga que Ranking es un número de 1 a 100 que es distinto para cada jugador. 
Si la tabla en un momento dado tiene solo 20 registros, indique cuantos registros tiene la tabla que resulta de la
siguiente consulta:
```
SELECT c1.Nombre, c2.Nombre
FROM PLAYERS c1, PLAYERS c2
WHERE c1.Ranking > c2.Ranking
```
Seleccione las respuestas correctas:

```
a) 400
b) 190
c) 20
d) imposible saberlo
```*/

-- RESPUESTA
Hay dos alternativas posibles
d) Imposible saberlo  [si tuviera que escoger una de las alternativas de forma obligatoria]

e) Ninguna de las anteriores ya que la cantidad de registros que tiene la tabla resultante es determinable como la sumatoria
de x, desde 2 hasta N, siendo N la cantidad de registros en la tabla.
En este caso, la cantidad de registros es de 209 con N=20                                                                */

