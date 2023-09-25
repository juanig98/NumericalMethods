from U6ApproximationByDifferentialEquations.methods.RungeKutta import RungeKutta4


def f(t, y):
    return t*y+1


l1,l2 = RungeKutta4(0, 1, 0.1, f)

print(l1)
print(l2)
