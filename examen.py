"""""
APUNTES DE EXAMEN – PYTHON
FUNCIONES · CICLOS · VALIDACIONES · TRY/EXCEPT
(Ejercicio X – listo para copiar y usar)

------------------------------------------------
CONCEPTOS CLAVE
- Uso funciones para modular y reutilizar código
- while: cuando NO conozco cuántos datos ingresan
- for: cuando la cantidad es conocida
- 0 como valor centinela para terminar
- try/except para evitar errores del usuario
- acumulador: suma valores
- contador: cuenta repeticiones
- None para inicializar mayor/menor
------------------------------------------------

VALIDACIONES Y TRY / EXCEPT

def leer_float(msg):
    """
    Lee un número decimal evitando errores de entrada.
    Úsalo siempre que el usuario escriba números.
    """
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Error: debe ingresar un número.")

def leer_entero(msg):
    """
    Lee un número entero validando errores.
    """
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Error: debe ingresar un entero.")

def division_segura():
    """
    División controlando errores comunes.
    """
    try:
        a = float(input("Numerador: "))
        b = float(input("Denominador: "))
        print("Resultado:", a / b)
    except ZeroDivisionError:
        print("Error: división por cero.")
    except ValueError:
        print("Error: entrada inválida.")

------------------------------------------------
OPERACIONES BÁSICAS

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

------------------------------------------------
PROMEDIOS Y ESTADÍSTICAS

def promedio_indefinido():
    """
    Promedio con cantidad indefinida (while + sentinela).
    """
    suma = 0
    cont = 0
    num = leer_float("Ingrese número (0 para terminar): ")

    while num != 0:
        suma += num
        cont += 1
        num = leer_float("Ingrese número (0 para terminar): ")

    if cont > 0:
        print("Promedio:", suma / cont)
    else:
        print("No se ingresaron datos.")

def promedio_definido():
    """
    Promedio con cantidad conocida (for).
    """
    n = leer_entero("Cantidad de números: ")
    suma = 0

    for i in range(n):
        suma += leer_float("Ingrese número: ")

    print("Promedio:", suma / n)

def numero_mayor():
    """
    Encuentra el número mayor.
    """
    mayor = None
    num = leer_float("Ingrese número (0 para terminar): ")

    while num != 0:
        if mayor is None or num > mayor:
            mayor = num
        num = leer_float("Ingrese número (0 para terminar): ")

    if mayor is not None:
        print("Número mayor:", mayor)
    else:
        print("No se ingresaron datos.")

def numero_menor():
    """
    Encuentra el número menor.
    """
    menor = None
    num = leer_float("Ingrese número (0 para terminar): ")

    while num != 0:
        if menor is None or num < menor:
            menor = num
        num = leer_float("Ingrese número (0 para terminar): ")

    if menor is not None:
        print("Número menor:", menor)
    else:
        print("No se ingresaron datos.")

def contar_pares_impares():
    """
    Cuenta números pares e impares.
    """
    pares = 0
    impares = 0
    num = leer_entero("Ingrese número (0 para terminar): ")

    while num != 0:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
        num = leer_entero("Ingrese número (0 para terminar): ")

    print("Pares:", pares)
    print("Impares:", impares)

------------------------------------------------
FIGURAS CON FOR

def triangulo(n):
    """
    Triángulo de altura n.
    """
    for i in range(1, n + 1):
        print("*" * i)

def cuadrado_lleno(n):
    """
    Cuadrado lleno.
    """
    for i in range(n):
        print("*" * n)

def cuadrado_hueco(n):
    """
    Cuadrado hueco.
    """
    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*")

------------------------------------------------
MENÚ BASE DE EXAMEN

def menu():
    print("""
1. Promedio indefinido
2. Número mayor
3. Número menor
4. Salir
""")

def leer_opcion():
    op = input("Opción: ")
    while not op.isdigit() or int(op) < 1 or int(op) > 4:
        print("Opción inválida.")
        op = input("Opción: ")
    return int(op)

def main():
    opcion = 0
    while opcion != 4:
        menu()
        opcion = leer_opcion()

        if opcion == 1:
            promedio_indefinido()
        elif opcion == 2:
            numero_mayor()
        elif opcion == 3:
            numero_menor()
        elif opcion == 4:
            print("Saliendo...")

------------------------------------------------
FRASES ÚTILES PARA RESPUESTAS TEÓRICAS

frases_examen = [
    "Uso funciones para modular el programa",
    "El while se usa cuando no conozco la cantidad de datos",
    "El for se usa cuando la cantidad es conocida",
    "Uso try-except para evitar errores del usuario",
    "Uso un valor centinela para finalizar el ciclo",
    "Uso acumulador y contador para cálculos",
    "Uso None para inicializar comparaciones",
    "La función main controla el flujo del programa"
]
------------------------------------------------
"""