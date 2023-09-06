"""
Modificar el programa de simulación de un servidor de cola simple, para
incorporar cada una de las siguientes modificaciones:
    a) La capacidad de la cola se limita a 10. Si una entidad que llega se 
        encuentra conla cola llena, se va del sistema.
    b) Hay dos servidores en paralelo, en lugar de uno. Las entidades usan
        el 1º servidor si los dos están disponibles. Determinar el tiempo 
        medio de utilización de cada servidor
    c) Hay 2 colas ante un único servidor. La entidad que arriba elije la 
        cola más corta. El servidor selecciona entidades de la cola más larga,
        para atender. Cuando ambas colas tienen la misma longitud, tanto las 
        entidades que llegan como el servidor, elijen la 1ª cola. 
        Se deben calcular los estadísticos de cada cola.
    d) Las entidades que esperan en la cola, abandonan el sistema si el tiempo 
        de espera excede 3 unidades de tiempo
"""

class Exercise:
    def resolve():
        pass