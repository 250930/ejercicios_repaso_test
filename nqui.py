def menu():
    print("""
          *** NEQUI ***
        
1. Cargar saldo
2. Pagar
3. Transferir dinero
4. Mostrar saldo
5. Salir
    """)

def leer_opcion():
    menu()
    op = input("Del 1 al 5, elija una opción: ")
    while not op.isdigit() or int(op) < 1 or int(op) > 5:
        print("Opción no válida")
        op = input("Digite un número del 1 al 5: ")
    return int(op)

def cargar_saldo(saldo):
    try:
        cantidad = int(input("¿Cuánto desea cargar?: $"))
        if cantidad <= 0:
            print("Monto inválido")
            return saldo
        saldo += cantidad
        print(f"Saldo actualizado: ${saldo}")
        return saldo
    except ValueError:
        print("Error: solo números")
        return saldo

def pagar(saldo):
    try:
        pago = float(input("Monto a pagar: $"))
        if pago <= 0:
            print("Monto inválido")
            return saldo
        if pago > saldo:
            print("Saldo insuficiente")
            return saldo
        saldo -= pago
        print(f"Pago realizado por ${pago}")
        print(f"Saldo actual: ${saldo}")
        return saldo
    except ValueError:
        print("Error: solo números")
        return saldo

def transferencia(saldo):
    try:
        celular = input("Ingrese el número de celular: ")
        if not celular.isdigit() or len(celular) != 10:
            print("Número inválido")
            return saldo

        monto = float(input("Monto a transferir: $"))
        if monto <= 0:
            print("Monto inválido")
            return saldo
        if monto > saldo:
            print("Saldo insuficiente")
            return saldo

        saldo -= monto
        print(f"Transferencia exitosa a {celular}")
        print(f"Saldo actual: ${saldo}")
        return saldo
    except ValueError:
        print("Error en los datos")
        return saldo

def cuenta(saldo):
    print("*" * 50)
    print(f"Saldo actual: ${saldo}")
    print("*" * 50)
def main():
    saldo = 0
    opcion = 0

    while opcion != 5:
        opcion = leer_opcion()

        if opcion == 1:
            saldo = cargar_saldo(saldo)
        elif opcion == 2:
            saldo = pagar(saldo)
        elif opcion == 3:
            saldo = transferencia(saldo)
        elif opcion == 4:
            cuenta(saldo)
        elif opcion == 5:
            print("Gracias por usar Nequi ")

        input("Presione ENTER para continuar...")
        print("\n" * 2)

if __name__ == "__main__":
    main()
