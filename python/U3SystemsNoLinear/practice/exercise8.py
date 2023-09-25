"""
Localice la raíz de f(x) = x^3 - 3x + 1 = 0; 
    por el método de Müller.
Aprox. {xi = 1; xi-1 = 1.5; xi-2 =2}
error: 0.001

"""


from U3SystemsNoLinear.methods.Muller import Muller


class ExerciseUsingMuller:
    def statement(self,):
        print("\nEjercicio 8")
        print("-"*80)
        print(
            "\nLocalice la raíz de f(x) = x^3 - 3x + 1 = 0; por el método de Müller.\nAprox. {xi = 1; xi-1 = 1.5; xi-2 =2}\nerror: 0.001\n")
        print("\nSolución")
        print("-"*80)

    def f(self, x):
        return x**3 - 3*x + 1

    xi = 1
    xi_1 = 1.5
    xi_2 = 2
    tol = 0.001
    max_iter = 20

    def resolve(self,):
        self.statement()
        print("Resultado: {}"
              .format(
                  Muller(
                      f=self.f,
                      epsilon=self.tol,
                      x0=self.xi,
                      x1=self.xi_1,
                      x2=self.xi_2,
                      max_iter=self.max_iter
                  )
              ))
