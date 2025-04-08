from literal import Literal
from clausula import Clausula
from base_conocimiento import BaseConocimiento

if __name__ == "__main__":
    # Crear literales
    A = Literal("A")
    noB = Literal("B", esta_negado=True)

    P = Literal("P")

    # Crear cláusula
    clausula1 = Clausula([A, noB])
    clausula2 = Clausula([P, P.negar()])

    # Crear base de conocimiento y agregar cláusula
    base = BaseConocimiento()
    base.agregar_clausula(clausula1)
    base.agregar_clausula(clausula2)

    print("Base de Conocimiento:")
    print(base)