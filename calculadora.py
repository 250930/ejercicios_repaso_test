def menu():
    print(""" CLACULADORA SENCILLA
SUMA
RESTA
MULTIPLICACION
DIVISION
SALIDA...
------------
OPCION: 1, 2, 3, 4, 5.""")


def leer_opciones():
    op = input()
    while (not op.isdigit() or int(op) < 1 or int(op) > 5):
        print("Error. Opcion no valida. Digite un numero de 1 a 5.")
        input("presione cualquier tecla para continuar...")
        print("\n\n")
        menu()
        op = input()

    return int(op)


def leer_float(msg):
    while (True):
        try:
            str_num = float(input(msg))
            return str_num
        except ValueError: 
            print("error. no es un numero float valido")
            input("intente nuevamentepresiando cualquier tecla...")


def suma():
    print("SUMA")

    n1 = leer_float("Ingrese el primer numero: ")
    n2 = leer_float("Ingrese el segundo numero: ")
    print(f"EL RESULTADO ES {n1 + n2}")
    return n1 + n2


def resta():
    print("RESTA")

    n1 = leer_float("Ingrese el primer numero: ")
    n2 = leer_float("Ingrese el segundo numero: ")
    print(f"EL RESULTADO ES {n1 - n2}")
    return n1 + n2


def multi():
    print("MULTIPLICACION")

    n1 = leer_float("Ingrese el primer numero: ")
    n2 = leer_float("Ingrese el segundo numero: ")
    print(f"EL RESULTADO ES {n1 * n2}")
    return n1 + n2


def divi():
    print("DIVISION")


    n1 = leer_float("Ingrese el primer numero: ")
    n2 = leer_float("Ingrese el segundo numero: ")
    print(f"EL RESULTADO ES {n1 / n2}")
    return n1 + n2

def main():
    opcion = 0
    while (opcion != 5):
        menu()
        opcion = leer_opciones()

        if opcion == 1:
            suma()

        elif opcion == 2:
            resta()

        elif opcion == 3:
            multi()

        elif opcion == 4:
            divi()

        elif opcion == 5:
            print("GRACIAS POR USAR EL PROGRAMA")

        input("PRESIONE CUALQUIER TECLA PARA CONTINUAR")