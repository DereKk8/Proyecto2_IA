from motor_inferencia import BaseConocimiento
from transformacion_fnc import convertir_a_fnc
from conversor_objetos import extraer_clausulas
from motor_resolucion import negar_conclusion, resolver_base

def main():
    print("=== Motor de Inferencia por Resolución ===\n")

    # Paso 1: Definir premisas (en formato lógico como tuplas)
    premisas = [
        ('→', 'A', 'B'),       # A → B
        ('→', 'B', 'C'),       # B → C
        'A'                    # A
    ]

    # Paso 2: Definir conclusión a probar
    conclusion = 'C'

    # Paso 3: Transformar premisas a FNC
    print("📌 Transformando premisas a FNC...\n")
    clausulas_objetos = []

    for p in premisas:
        fnc = convertir_a_fnc(p)
        print(f"FNC de {p} => {fnc}")
        clausulas = extraer_clausulas(fnc)
        clausulas_objetos.extend(clausulas)

    # Paso 4: Negar conclusión y convertir a FNC
    print(f"\n📌 Negando la conclusión '{conclusion}' y transformando a FNC...\n")
    negada = negar_conclusion(conclusion)
    fnc_negada = convertir_a_fnc(negada)
    print(f"FNC de ¬{conclusion} => {fnc_negada}")
    clausulas_negadas = extraer_clausulas(fnc_negada)
    clausulas_objetos.extend(clausulas_negadas)

    # Paso 5: Crear base de conocimiento
    base = BaseConocimiento()
    for c in clausulas_objetos:
        base.agregar_clausula(c)

    print("\n📚 Base de Conocimiento Inicial:")
    print(base)

    # Paso 6: Ejecutar resolución
    print("\n🚀 Ejecutando motor de inferencia...\n")
    resultado, pasos = resolver_base(base)

    print("\n📝 Registro de pasos:")
    for paso in pasos:
        print(" -", paso)

    if resultado:
        print("\n✅ Conclusión derivada: La conclusión ES consecuencia lógica de las premisas.")
    else:
        print("\n❌ Conclusión NO derivada: La conclusión NO es consecuencia lógica de las premisas.")

if __name__ == "__main__":
    main()