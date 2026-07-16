1. Collections

El módulo collections es una biblioteca de la librería estándar de Python que proporciona estructuras de datos especializadas. Aunque Python ya incluye tipos como listas (list), diccionarios (dict), tuplas (tuple) y conjuntos (set), en muchas situaciones estas estructuras no son la mejor opción. El módulo collections ofrece alternativas más eficientes, más legibles o con funcionalidades adicionales para resolver problemas comunes.

¿Cuándo usar collections?

Debes considerar usar collections cuando notes que una estructura de datos normal requiere demasiado código para hacer una tarea sencilla o cuando necesites funcionalidades que las estructuras básicas no ofrecen.

Por ejemplo:

Cuando necesitas contar cuántas veces aparece un elemento, usar un diccionario funciona, pero Counter lo hace automáticamente.
Cuando quieres un diccionario que cree valores por defecto sin generar errores, defaultdict es la mejor opción.
Cuando deseas almacenar datos de manera similar a una clase, pero sin escribir una clase completa, namedtuple es una solución sencilla y eficiente.
Cuando necesitas una cola o una pila muy rápida para insertar y eliminar elementos por ambos extremos, deque es mucho más eficiente que una lista.
¿Por qué existe collections?

Muchas veces los programadores escribían el mismo código una y otra vez para resolver problemas comunes. El módulo collections nació para ofrecer soluciones ya implementadas, optimizadas y fáciles de leer.

Ventajas de usar collections

Reduce la cantidad de código.
Hace el programa más legible.
Evita errores comunes.
Ofrece mejor rendimiento en ciertos casos.
Permite expresar claramente la intención del código.