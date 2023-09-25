import math


def Muller(f, x0, x1, x2, epsilon=1e-10, max_iter=100):
    h1 = x1 - x0
    h2 = x2 - x1
    y1 = (f(x1) - f(x0)) / h1
    y2 = (f(x2) - f(x1)) / h2
    d = (y2 - y1) / (h2 + h1)
    n_iter = 3
    x = None
    while n_iter <= max_iter:
        b = y2 + h2*d
        D = math.sqrt(b**2 - 4*f(x2)*d)
        if abs(b-D) < abs(b+D):
            E = b + D
        else:
            E = b - D
        h = -2*f(x2)/E
        p = x2 + h
        if abs(h) < epsilon:
            x = p
            break
        x0, x1, x2 = x1, x2, p
        h1 = x1 - x0
        h2 = x2 - x1
        y1 = (f(x1) - f(x0)) / h1
        y2 = (f(x2) - f(x1)) / h2
        d = (y2 - y1) / (h2 + h1)
        n_iter += 1
    if x is None:
        raise ValueError("El método no converge")
    return x
