# aqui se decidio utilizar h en lugar de dt para el incremento
def RungeKutta2(x0, t_final, h, f):
    lista_t = []
    lista_x = []

    x = x0
    t = 0.

    while t < t_final+h:		# para incluir t_final
        lista_t.append(t)
        lista_x.append(x)

        k1 = f(x, t)
        k2 = f(x + 0.5*h*k1, t+0.5*h)

        x += h * k2
        t += h

    return lista_t, lista_x


def RungeKutta4(x0, t_final, h, f):
    lista_t = []
    lista_x = []

    x = x0
    t = 0.

    while t < t_final+h:		# para incluir t_final
        lista_t.append(t)
        lista_x.append(x)

        k1 = f(x, t)
        k2 = f(x + 0.5*h*k1, t+0.5*h)
        k3 = f(x + 0.5*h*k2, t+0.5*h)
        k4 = f(x + h*k3, t+h)

        x += h/6. * (k1 + 2.*k2 + 2.*k3 + k4)
        t += h

    return lista_t, lista_x
