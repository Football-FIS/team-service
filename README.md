# Team Service

## Descripción
Uno de los pilares fundamentales de la aplicación es permitir que los usuarios creen un
equipo al cual agregar jugadores y futuros partidos.

Este microservicio es el encargado de gestionar todo lo relacionado con el equipo, y
por consiguiente, todo lo relacionado con la autentificación de los usuarios.

Las principales funcionalidades de nuestro servicio son las siguientes:
- CRUD de Team (GET, POST, PUT y DELETE)
- Autentificación de los usuarios mediante Google.
- Validación de tokens (API Gateway de Autentificación)
- Validación de feature toggles.

## Documentación (Swagger)
Los distintos endpoints disponibles en nuestro servicio pueden ser observados
en la ruta /api/v1/docs.

Además se podrá observar las entradas y salidas esperadas.

## Nivel y Características
Se han implementado las características necesarias para llegar a 9 puntos.

A continuación, vamos a indicar las características realizadas y se indicará en que lugar
del código se puede observar su implementación.

### Características de microservicio avanzado
Se debían implementar como mínimo 5 características.

#### Implementar un frontend con rutas y navegación
Hemos optado por realizar un frontend común para todos los proyectos, este proyecto se puede encontrar 
en este mismo repositorio, footmach-frontend.

Hemos desarrollado los siguientes componentes:
- create-team: accesible desde url/create-team
- my-profile: componente implementado en profile
- profile: accesible desde url/profile
- team-service: accesible desde url/login
- update-team: accesible desde url/update-team

#### Implementar caché
Hemos optado por implementar una caché para este microservicio haciendo uso de Redis.

El proyecto puede ser encontrado en este mismo repositorio con el nombre redis-team-service.

La conexión de ambos servicio se puede observar en team_service/team_service/settings.py
línea 201.

#### Consumir alguna API externa
La API externa consumida por nuestro servicio es el sistema de autentificación
de Google.

La librería utilizada ha sido dj_rest_auth. Las distintas keys están almacenadas en base
de datos.

Esto permite verificar que el code proporcionado por el usuario es válido.

#### Mecanismo de autenticación basado en JWT
Para implementar el mecanismo de autentificación hemos utilizado la librería allauth.

La configuración se ha realizado en team_service/team_service/settings.py línea 59.

Por defecto, todas las vistas se encuentran protegidas.

La autentificación con JWT y la utilización de Google están sumamente relacionadas.

#### Feature toggles
Nuestro proyecto dispone de distintos planes de precio y cada uno de estos planes
permite realizar unas acciones y otras.

Nuestro servicio es el encargado de verificar si las distintas peticiones son válidas.

Un ejemplo de comprobación de plan se puede observar en team_service/api/v1/views.py
línea 43.

#### Extensión de microservicio (Docker Service)
Durante el desarrollo del trabajo nos dimos cuenta de la dificultad de manejar distintos microservicios
en local.

Por ello se creó un nuevo proyecto en este mismo repositorio llamado docker-service.

Este permite mediante instrucciones en consola (make up-team) desplegar un servicio
de una manera sencilla, o (make-all) desplegar todos con un simple comando.

Además podemos añadir un frag extra (make up-team-logs) que permite ver los logs
de un microservicio de una manera sencilla.

### Aplicación basada en microservicios avanzada
Se debian implementar como mínimo 3 características.

#### Frontend común
Se puede encontrar el frontend en este mismo repositorio, llamado footmatch-frontend.

#### Implementación de un mecanismo de autenticación homogéneo para todos los microservicios
Como ya explicamos anteriormente, nuestro servicio además de comportarse como CRUD, es el encargado
de realizar la auntentificación de los distintos microservicios.

Todos los microservicio podrán verificar si un usuario puede realizar una acción
realizando peticiones sobre nuestro endpoint api/v1/validate-token.

Se puede observar su desarrollo en el archivo team_service/api/v1/views.py en la 
línea 29.

#### Realizar pruebas de integración con otros microservicios
Este servicio está integrado con Player Service para el envio de correos a los jugadores
que tienen un partido en las próximas horas.

Los test realizados con este servicio se pueden ver en team_service/api/v1/tests/integration/test_send_email_player.py.

Además de estos se han realizado test de integración con la base de datos. Se pueden encontrar
en la carpeta team_service/api/v1/tests/integration/.

#### Electron
Una vez terminada la aplicación se procedió a compilarla para que pudiese ser utilizada
como una aplicación nativa de Windows (.exe)
