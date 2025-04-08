class Literal:
    def __init__(self, nombre: str, esta_negado: bool = False):
        self.nombre = nombre
        self.esta_negado = esta_negado

    def negar(self):
        return Literal(self.nombre, not self.esta_negado)

    def __eq__(self, otro):
        return isinstance(otro, Literal) and self.nombre == otro.nombre and self.esta_negado == otro.esta_negado

    def __hash__(self):
        return hash((self.nombre, self.esta_negado))

    def __str__(self):
        return f"¬{self.nombre}" if self.esta_negado else self.nombre

    def __repr__(self):
        return str(self)