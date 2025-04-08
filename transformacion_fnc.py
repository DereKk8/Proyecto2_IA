# transformacion_fnc.py

def eliminar_implicaciones(expresion):
    if isinstance(expresion, str):
        return expresion
    operador, *operandos = expresion

    if operador == '→':
        A, B = operandos
        return ('∨', ('¬', eliminar_implicaciones(A)), eliminar_implicaciones(B))
    else:
        return (operador, *(eliminar_implicaciones(op) for op in operandos))


def mover_negaciones(expresion):
    if isinstance(expresion, str):
        return expresion

    operador, *operandos = expresion

    if operador == '¬':
        subexpresion = operandos[0]
        if isinstance(subexpresion, str):
            return ('¬', subexpresion)
        sub_op, *sub_args = subexpresion

        if sub_op == '¬':
            return mover_negaciones(sub_args[0])
        elif sub_op == '∧':
            return ('∨', *[mover_negaciones(('¬', arg)) for arg in sub_args])
        elif sub_op == '∨':
            return ('∧', *[mover_negaciones(('¬', arg)) for arg in sub_args])
        else:
            return ('¬', mover_negaciones(subexpresion))
    else:
        return (operador, *(mover_negaciones(op) for op in operandos))


def distribuir_ors(expresion):
    if isinstance(expresion, str) or (isinstance(expresion, tuple) and expresion[0] == '¬'):
        return expresion

    operador, *operandos = expresion
    if operador == '∨':
        A = distribuir_ors(operandos[0])
        B = distribuir_ors(operandos[1])

        if isinstance(A, tuple) and A[0] == '∧':
            return ('∧', *(distribuir_ors(('∨', a, B)) for a in A[1:]))
        elif isinstance(B, tuple) and B[0] == '∧':
            return ('∧', *(distribuir_ors(('∨', A, b)) for b in B[1:]))
        else:
            return ('∨', A, B)

    elif operador == '∧':
        return ('∧', *(distribuir_ors(op) for op in operandos))

    return expresion


def convertir_a_fnc(expresion):
    sin_implicaciones = eliminar_implicaciones(expresion)
    sin_negaciones = mover_negaciones(sin_implicaciones)
    fnc = distribuir_ors(sin_negaciones)
    return fnc