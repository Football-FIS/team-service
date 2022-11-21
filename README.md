# Team Service

## Requisitos
- Python > 3.8
- Docker

## Instalación

### Github
Primero debes clonar el repositorio:

```sh
$ git@github.com:Football-FIS/team-service.git
$ cd team-service
```

### Docker
Primero debes crear un archivo __.env__ con el mismo formato que 
__.env.example__.

En este archivo se declararán las variables de entorno para lanzar el
servicio.

Se ha creado un archivo __Makefile__ el cual simplificará el funcionamiento
de docker.

```sh
$ make start # Arrancar el servicio en segundo plano.
```
```sh
$ make start-logs # Arrancar el servicio y ver la consola.
```
```sh
$ make stop # Detener el servicio.
```
```sh
$ make status # Ver el estados de los servicios.
```

Si haces un `make start` o `start-logs` podrás acceder a la url 
`http://localhost:8000/` y ver la pantalla principal de Django.
