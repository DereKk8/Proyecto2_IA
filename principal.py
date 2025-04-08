# pruebas_transformacion.py

from transformacion_fnc import convertir_a_fnc

from motor_inferencia import Literal

def pruebas_fnc():
    ejemplos = [
        ("Implicación simple", ('→', 'A', 'B'), ('∨', ('¬', 'A'), 'B')),
        ("Doble negación", ('¬', ('¬', 'A')), 'A'),
        ("De Morgan AND", ('¬', ('∧', 'A', 'B')), ('∨', ('¬', 'A'), ('¬', 'B'))),
        ("De Morgan OR", ('¬', ('∨', 'A', 'B')), ('∧', ('¬', 'A'), ('¬', 'B'))),
        ("Distribución OR sobre AND", ('∨', 'A', ('∧', 'B', 'C')), ('∧', ('∨', 'A', 'B'), ('∨', 'A', 'C')))
    ]

    A = Literal("P", True)

    for nombre, entrada, esperado in ejemplos:
        resultado = convertir_a_fnc(entrada)
        print(f"[{nombre}]")
        print("Entrada:   ", entrada)
        print("Esperado:  ", esperado)
        print("Resultado: ", resultado)
        print("¿Correcto?:", resultado == esperado)
        print("---")

    print(A.__neg__())

if __name__ == "__main__":
    pruebas_fnc()