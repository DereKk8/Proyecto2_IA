from motor_inferencia import Clausula
import itertools

def negar_conclusion(conclusion):
    """
    Niega una conclusión para aplicar resolución por refutación.
    Si ya está negada, quita la negación (doble negación).
    """
    if isinstance(conclusion, tuple) and conclusion[0] == '¬':
        return conclusion[1]
    return ('¬', conclusion)


def son_complementarios(lit1, lit2):
    """
    Verifica si dos literales son complementarios:
    mismo nombre, diferente signo (uno negado, otro no).
    """
    return lit1.nombre == lit2.nombre and lit1.negado != lit2.negado


def resolver(cl1, cl2):
    """
    Aplica la regla de resolución entre dos cláusulas.
    Retorna una lista de cláusulas resultantes (resolventes).
    """
    resolventes = []
    for lit1 in cl1.literales:
        for lit2 in cl2.literales:
            if son_complementarios(lit1, lit2):
                nuevos_lits = set(cl1.literales | cl2.literales)
                nuevos_lits.discard(lit1)
                nuevos_lits.discard(lit2)
                nueva_clausula = Clausula(list(nuevos_lits))
                resolventes.append(nueva_clausula)
    return resolventes


def obtener_pares(clausulas):
    """
    Genera todos los pares únicos de cláusulas.
    """
    return list(itertools.combinations(clausulas, 2))


def es_clausula_vacia(clausula):
    """
    Verifica si una cláusula no contiene literales.
    """
    return len(clausula.literales) == 0


def resolver_base(base):
    """
    Algoritmo principal de resolución por refutación.
    Devuelve una tupla (esDerivable, historial de pasos).
    """
    nuevos = set()
    historial = []

    while True:
        pares = obtener_pares(base.clausulas)
        for (ci, cj) in pares:
            resolventes = resolver(ci, cj)
            for r in resolventes:
                historial.append(f"{ci} + {cj} => {r}")
                if es_clausula_vacia(r):
                    print("💥 Se encontró cláusula vacía. La conclusión es válida.")
                    return True, historial
                if r not in base.clausulas and r not in nuevos:
                    nuevos.add(r)

        if nuevos.issubset(set(base.clausulas)):
            print("❌ No se pudo derivar la cláusula vacía. No se puede probar la conclusión.")
            return False, historial

        base.clausulas.extend(nuevos)
        nuevos.clear()