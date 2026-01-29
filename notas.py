def menu():
    print("""
CALCULAR NOTAS
1. PROMEDIO NOTAS
2. NOTA MAS ALTA
3. NOTA MAS BAJA
4. SALIR
------------
OPCION: 1, 2, 3, 4
""")


def leer_opciones():
    op = input("Digite una opción: ")
    while not op.isdigit() or int(op) < 1 or int(op) > 4:
        print("Error. Opción no válida. Digite un número de 1 a 4.")
        input("Presione cualquier tecla para continuar...")
        menu()
        op = input("Digite una opción: ")
    return int(op)


def leer_nota(msg):
    while True:
        try:
            nota = float(input(msg))
            if nota < 0:
                print("La nota no puede ser negativa.")
            else:
                return nota
        except ValueError:
            print("Error. No es un número válido.")
            input("Presione cualquier tecla para intentar nuevamente...")


def promedio():
    cont = 0
    suma = 0

    nota = leer_nota("Ingrese la nota (0 para terminar): ")

    while nota != 0:
        cont += 1
        suma += nota
        nota = leer_nota("Ingrese la nota (0 para terminar): ")

    if cont > 0:
        prom = suma / cont
        print("El promedio de las notas es:", prom)
    else:
        print("No se ingresaron notas.")


def mayor():
    mayor = None
    nota = leer_nota("Ingrese la nota (0 para terminar): ")

    while nota != 0:
        if mayor is None or nota > mayor:
            mayor = nota
        nota = leer_nota("Ingrese la nota (0 para terminar): ")

    if mayor is not None:
        print("La nota más alta es:", mayor)
    else:
        print("No se ingresaron notas.")


def menor():
    menor = None
    nota = leer_nota("Ingrese la nota (0 para terminar): ")

    while nota != 0:
        if menor is None or nota < menor:
            menor = nota
        nota = leer_nota("Ingrese la nota (0 para terminar): ")

    if menor is not None:
        print("La nota más baja es:", menor)
    else:
        print("No se ingresaron notas.")


def main():
    opcion = 0
    while opcion != 4:
        menu()
        opcion = leer_opciones()

        if opcion == 1:
            promedio()
        elif opcion == 2:
            mayor()
        elif opcion == 3:
            menor()
        elif opcion == 4:
            print("GRACIAS POR USAR EL PROGRAMA")

        input("Presione cualquier tecla para continuar...")


main()
