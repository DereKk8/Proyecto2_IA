from motor_inferencia import Literal, Clausula

def es_literal(expresion):
    """
    Verifica si la expresión es un literal, es decir:
    - una cadena: 'A'
    - una negación simple: ('¬', 'A')
    """
    if isinstance(expresion, str):
        return True
    if isinstance(expresion, tuple) and expresion[0] == '¬' and isinstance(expresion[1], str):
        return True
    return False


def crear_literal(expresion):
    """
    Convierte una expresión como 'A' o ('¬', 'A') en un objeto Literal.
    """
    if isinstance(expresion, str):
        return Literal(expresion)
    elif isinstance(expresion, tuple) and expresion[0] == '¬':
        return Literal(expresion[1], negado=True)
    else:
        raise ValueError(f"Expresión no válida como literal: {expresion}")


def extraer_clausulas(fnc):
    """
    Toma una expresión FNC como:
        ('∧', ('∨', '¬A', 'B'), ('∨', 'C', 'D'))
    Y devuelve una lista de objetos Clausula:
        [
            Clausula([Literal('A', True), Literal('B')]),
            Clausula([Literal('C'), Literal('D')])
        ]
    """
    clausulas = []

    if isinstance(fnc, tuple) and fnc[0] == '∧':
        for subexp in fnc[1:]:
            clausulas.append(crear_clausula(subexp))
    else:
        # Caso de una sola cláusula (sin ∧)
        clausulas.append(crear_clausula(fnc))

    return clausulas


def crear_clausula(expresion):
    """
    Toma una subexpresión disyuntiva y devuelve un objeto Clausula.
    Ej:
        ('∨', '¬A', 'B') → Clausula([¬A, B])
        'A' → Clausula([A])
    """
    literales = []

    if es_literal(expresion):
        literales.append(crear_literal(expresion))

    elif isinstance(expresion, tuple) and expresion[0] == '∨':
        for subexp in expresion[1:]:
            literales.append(crear_literal(subexp))
    else:
        # Si no es una disyunción, puede ser un único literal o negación
        literales.append(crear_literal(expresion))

    return Clausula(literales)