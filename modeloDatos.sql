CREATE TABLE Profesor (
	rut INTEGER NOT NULL,
	nombre VARCHAR(25) NOT NULL,
	apellido VARCHAR(25) NOT NULL
);
ALTER TABLE Profesor ADD PRIMARY KEY(`rut`);

CREATE TABLE Alumno (
	rut INTEGER NOT NULL,
	nombre VARCHAR(25) NOT NULL,
	apellido VARCHAR(25) NOT NULL
);
ALTER TABLE Alumno ADD PRIMARY KEY(`rut`);
ALTER TABLE `alumno` ADD PRIMARY KEY(`rut`);

CREATE TABLE Curso (
	id INTEGER NOT NULL,
	rutProfesor INTEGER,
	nombre VARCHAR(50)
);
ALTER TABLE Curso ADD PRIMARY KEY(`id`);
ALTER TABLE ADD CONSTRAINT `curso_profesor_rut_fk` FOREIGN KEY(`rutProfesor`) REFERENCES `Profesor`(`rut`) ON DELETE NO ACTION ON UPDATE CASCADE;


CREATE TABLE Prueba (
	id INTEGER,
	idCurso INTEGER,
	materia VARCHAR(25)
);
ALTER TABLE Prueba ADD CONSTRAINT `prueba_curso_id_fk` FOREIGN KEY(`idCurso`) REFERENCES `Curso`(`id`) ON UPDATE CASCADE;

CREATE TABLE CursoAlumno (
	idCA INTEGER,
	idCurso INTEGER,
	rutAlumno INTEGER,
);
ALTER TABLE CursoAlumno ADD PRIMARY KEY (`idCA`);
ALTER TABLE CursoAlumno ADD CONSTRAINT `curso_alumno_prueba_id_fk` FOREIGN KEY (`idCurso`) REFERENCES `Curso`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE CursoAlumno ADD CONSTRAINT `curso_alumno_rut_fk` FOREIGN KEY (`rutAlumno`) REFERENCES `Alumno`(`rut`) ON DELETE NO ACTION ON UPDATE CASCADE;

CREATE TABLE CursoPruebaAlumno (
	idCursoAlumno INTEGER NOT NULL,
	idPrueba INTEGER NOT NULL,
	nota DECIMAL NOT NULL	
);
ALTER TABLE CursoPruebaAlumno ADD CONSTRAINT `curso_alumno_prueba_curso_alumno_id_fk` FOREIGN KEY (`idCursoAlumno`) REFERENCES `CursoAlumno`(`rutAlumno`) ON UPDATE CASCADE;
ALTER TABLE CursoPruebaAlumno ADD CONSTRAINT `alumno_prueba_id_fk` FOREIGN KEY(`idPrueba`) REFERENCES `Prueba`(`id`) ON UPDATE CASCADE;