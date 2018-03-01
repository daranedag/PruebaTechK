# Sobre el Test
Las diferentes preguntas que se encuentran en al archivo "README.md" fueron respondidas y desarrolladas en distintas carpetas y/o archivos que se detallan a continuación.

## Modelo de datos
El modelo de datos se encuentra en el archivo "modeloDatos.sql"
que contiene todos los create y alter utilizados para el modelo.

## SQL
Las respuestas en SQL Server se encuentran en el archivo "preguntaSQL.sql"
Cada pregunta se encuentra escrita como comentario de dicho archivo y las respuestas sin comentar.
La última pregunta de esta sección tuvo 2 respuestas posibles que estaán aclaradas en el archivo antes mencionado y dado el tipo de respuesta entregado , esta es la única respuesta que se encuentra comentada.

	Nota: Se incluyó un archivo "BDsPrueba.xlsx" con el fin de hacer pruebas correspondientes al ingreso de datos, claves foraneas, primraias, y visualización de los datos.

## Diseño de Software
Para ambos requerimientos se utilizó bootstrap como librería de CSS.
###Backend
	Para poder iniciar el proyecto se necesita una terminal abierta (Ubuntu, Windows)
	posicionarse en la carpeta TechK/Colegio y ejecutar los siguientes comandos en el orden indicado.
	[Se asume que Django se encuentra instalado con su version 2.0.2 que fue la utilizada para este desarrollo]
	------Ubuntu--------
	1) python3 manage.py makemigrations
	2) python3 manage.py migrate
	2) python3 manage.py runserver

	------Windows---
	1) python manage.py makemigrations
	2) python manage.py migrate
	2) python manage.py runserver

	Importante: las vistas de Promedio rojos no se encuentran habilitadas debido a un error con la BD
	al momento de realizar la consulta y pasar el resultado de dicha query a la vista.
	Ambas query para obtener los datos solicitados se encuentran bajo en el archivo /Colegio/crud/

###FrontEnd
	El frontend se dasrroollo sin problemas mayores, ya que se utilizó JS y JSON principal
	Este se encuentra bajo la carpeta TechK/FrontEnd/index.html
	Para poder visualizar este proyecto se debe abrir el index.html con el navegador
