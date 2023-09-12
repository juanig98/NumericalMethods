"""
Dados los tres puntos del plano 
    P0(0,-2)
    P1(1,6)
    P2(3,40)

Encontrar el polinomio interpolado de Lagrange que pase por ellos.
Rta: 3x^2 + 5x - 2


"""


from U4InterpolationAndAproximation.methods.Lagrange import LagrangePol


class ExerciseUsingLagrange:
    def statement(self,):
        print("\nEjercicio 1")
        print("-"*80)
        print(
            "\nDados los tres puntos del plano \n\tP0(0,-2)\n\tP1(1,6)\n\tP2(3,40)\n\nEncontrar el polinomio interpolado de Lagrange que pase por ellos.\nRta: 3x^2 + 5x - 2\n")
        print("\nSolución")
        print("-"*80)

    x = [0,1,3]
    y = [-2,6,40]
    

    def resolve(self,):
        self.statement()
            
        print("Resultado: {}"
              .format(Pf.__str__))
