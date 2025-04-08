from literal import Literal

class Clausula:
    def __init__(self, literales=None):
        self.literales = set(literales) if literales else set()

    def agregar_literal(self, literal: Literal):
        self.literales.add(literal)

    def __contains__(self, literal):
        return literal in self.literales

    def __iter__(self):
        return iter(self.literales)

    def __len__(self):
        return len(self.literales)

    def __str__(self):
        return ' ∨ '.join(str(lit) for lit in sorted(self.literales, key=lambda x: x.nombre))

    def __repr__(self):
        return f"Clausula({self.literales})"