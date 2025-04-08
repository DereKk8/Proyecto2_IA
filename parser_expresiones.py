import re
from motor_inferencia import Negacion, Conjuncion, Disyuncion, Implicacion

def parsear_expresion(expresion_str: str):
    expresion_str = expresion_str.replace(" ", "")
    return _parsear(expresion_str)

def _parsear(exp):
    # Caso base: literal (A, B, C...)
    if re.fullmatch(r"[a-zA-Z][a-zA-Z0-9]*", exp):
        return exp

    # Negación: ¬A o ~A
    if exp.startswith("-") or exp.startswith("~"):
        return Negacion(_parsear(exp[1:]))

    # Quitar paréntesis envolventes
    if exp.startswith("(") and exp.endswith(")"):
        exp = exp[1:-1]

    # Buscar operadores principales (fuera de paréntesis anidados)
    nivel = 0
    for i in range(len(exp)):
        if exp[i] == '(':
            nivel += 1
        elif exp[i] == ')':
            nivel -= 1
        elif nivel == 0:
            if exp[i:i+2] == "→" or exp[i:i+2] == "=>":
                izquierda = _parsear(exp[:i])
                derecha = _parsear(exp[i+2:])
                return Implicacion(izquierda, derecha)
            elif exp[i] == "∨" or exp[i] == "|":
                izquierda = _parsear(exp[:i])
                derecha = _parsear(exp[i+1:])
                return Disyuncion(izquierda, derecha)
            elif exp[i] == "∧" or exp[i] == "&":
                izquierda = _parsear(exp[:i])
                derecha = _parsear(exp[i+1:])
                return Conjuncion(izquierda, derecha)

    raise ValueError(f"Expresión mal formada: {exp}")