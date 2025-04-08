# motor_inferencia.py

class Literal:
    """
    Representa un literal lógico.
    Un literal puede ser un átomo (por ejemplo, A) o su negación (¬A).
    """
    def __init__(self, nombre, negado=False):
        self.nombre = nombre
        self.negado = negado

    def __eq__(self, otro):
        return isinstance(otro, Literal) and self.nombre == otro.nombre and self.negado == otro.negado

    def __hash__(self):
        return hash((self.nombre, self.negado))

    def __neg__(self):
        """Devuelve el literal negado."""
        return Literal(self.nombre, not self.negado)

    def __str__(self):
        return f"¬{self.nombre}" if self.negado else self.nombre

    def __repr__(self):
        return str(self)


class Clausula:
    """
    Representa una cláusula: un conjunto de literales conectados por OR.
    Ejemplo: A ∨ ¬B ∨ C
    """
    def __init__(self, literales=None):
        self.literales = set(literales) if literales else set()

    def agregar_literal(self, literal):
        self.literales.add(literal)

    def esta_vacia(self):
        return len(self.literales) == 0

    def __contains__(self, literal):
        return literal in self.literales

    def __str__(self):
        if self.esta_vacia():
            return "⊥"  # Cláusula vacía (falsedad)
        return " ∨ ".join(str(lit) for lit in self.literales)

    def __repr__(self):
        return str(self)


class BaseDeConocimientos:
    """
    Representa la base de conocimientos del sistema.
    Contiene un conjunto de cláusulas en FNC.
    """
    def __init__(self):
        self.clausulas = []

    def agregar_clausula(self, clausula):
        self.clausulas.append(clausula)

    def cargar_desde_lista(self, lista_de_clausulas):
        """Carga múltiples cláusulas a partir de una lista."""
        for clausula in lista_de_clausulas:
            self.agregar_clausula(clausula)

    def __str__(self):
        return "\n".join(f"Cláusula {i+1}: {str(c)}" for i, c in enumerate(self.clausulas))