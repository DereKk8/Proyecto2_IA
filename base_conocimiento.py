from clausula import Clausula

class BaseConocimiento:
    def __init__(self):
        self.clausulas = []

    def agregar_clausula(self, clausula: Clausula):
        self.clausulas.append(clausula)

    def __iter__(self):
        return iter(self.clausulas)

    def __str__(self):
        return '\n'.join(f"{i+1}: {clausula}" for i, clausula in enumerate(self.clausulas))

    def __len__(self):
        return len(self.clausulas)