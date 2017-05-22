# Shallow-Water-2D-Equations #

Este paquete contiene lo básico para poder simular las ecuaciones de aguas someras (Shallow Water Equations) en dos dimensiones. Se adjuntan también algunos vídeos de distintas variables, junto con los valores que se han introducido para conseguir esas animaciones.

## Requerimientos

Compatible con Python 3.5 y Python 2.7. Es necesario ejecutar

```bash
$ pip install -r requirements.txt
```

Además, es necesario instalar ffmpeg

```bash
$ sudo apt install ffmpeg
```

## Teoría

Para simular estas ecuaciones se ha usado el Método de Volúmenes Finitos. Se han implementado los flujos de Godunov, HLL y Lax-Friedrich.

Las ecuaciones de Shallow Water son una simplificación de las ecuaciones de Navier-Stokes. Este paquete fue desarollado para el Trabajo de Fin de Grado de Carlos Perales, Graduado en Física por la Universidad de Córdoba. Se puede acceder a documentación teórica [aquí](http://es.slideshare.net/CarlosPerales/estudio-y-simulacin-numrica-de-las-ecuaciones-de-aguas-someras)

## Vídeos

Algunos vídeos generados con este programa pueden verse en esta lista de reproducción de [Youtube](https://www.youtube.com/watch?v=ConQO-z8Ks4&list=PLkjZXk8AWCPW18dZUjr093jvvx3NUvY5l)

## Licencia:

http://www.gnu.org/licenses/gpl-3.0.txt
