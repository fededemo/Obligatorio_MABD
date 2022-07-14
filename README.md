# Obligatorio creado para materia Modelos Avanzados de Base de Datos. 

Repo que contiene el codigo para una tarea que consistia en realizar la implementación para el almacenamiento de un subsistema de Catalogo de Productos simulado para Tesla.

Tal como se planteaba en la consigna, el mismo debe mantener todos los productos que se fabrican y/o comercializan desde el sitio web. Se debia buscar que el motor de base de datos soportara la operativa, brindara alta disponibilidad y flexibilidad para introducir cambios sin el riesgo de tiempos muertos.

Dado lo anterior, el almacenamiento elegido fue MongoDB. 

La programación contenida en este repo fue realizada en Python con la librería flask (utilizando también html y algo de js) y se usó DigitalOcean para crear la base y hostear el aplicativo. 

Una vez ingresado al aplicativo, en la sección inicial o Crear Nuevo Producto se pueden cargar los datos pertenecientes a un próximo lanzamiento y una vez realizado el submit correspondiente, el mismo se agregará a la base:

![alt text](https://lh6.googleusercontent.com/_zrGSGD7NUkID6oLFw5AoCHFmUvTbtkHXQ_xs-VGGHJw5mCGz7u6hnkGN67SsvP2uxXjxUFlYUQyieAlCAh5zf45drYmd0tGkbvZ26qiOSPuLz_CX1IX4gsRvNrWzkqm5NxJLxrUhfwpz1D-EecV4JM)

En la sección Ver Catálogo Actual se pueden observar los datos de toda la base y concretamente los de la nueva inserción:

![alt text](https://lh5.googleusercontent.com/JvMYnGJYJanweWYpNJVsJWhP17kQP64F20Xp4ANWjjenpocZ38qpGRjan03LX-HEJT42Kre2zj3X4kuhAneJZvwTwYFkZCFnQTsBVYpxDAvNsCtqv08vwM8AFLzFMuAlopdC8LKUr6swyNOc9rovmNU)
