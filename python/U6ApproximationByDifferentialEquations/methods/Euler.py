
# Codigo para implementar los distintos metodos para la tarea 2
# Las funciones euler etc. funcionan de manera **igual** para ecuaciones
# de orden superior si utilizamos *vector 



	
def Euler(x0, t_final, dt, f):
    lista_t  = []
    lista_x = []
    
    x = x0
    t = 0.

    while t < t_final+dt:
        lista_t.append(t)
        lista_x.append(x)
        x += dt * f(x,t)
        t += dt

    return lista_t, lista_x