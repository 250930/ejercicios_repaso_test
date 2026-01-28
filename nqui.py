def menu():
    print("""
          ***NEQUI***
        
        1. Cargar saldo
        2. Pagar
        3. Transferir dinero
        4. Mostrar saldo
        5. Salir
        
        """)

def leer_opcion():
    menu()
    op = input()
    while(not op.isdigit() or int(op)<1 or int(op)>5):
        print("Opción no válida, digite un número del 1 al 5: ")
        input("Presione cualquier tecla para continuar...")
        print("\n\n")
        menu()
        op = input()

    return int(op)

def cargar_saldo(saldo):
        try:    
            cantidad =int(input("cuanto va a ingresar a su saldo"))
            if cantidad <= 0:
                print("ingrese un monto valido, debe ser por encima de $0")
                return saldo
            cantidad += saldo
            print(f"""su saldo se actualizo
                su saldo actual es {saldo}""")
        except ValueError:
            print("error")
            return saldo
        
def pagar(saldo):
    try:
        pago = float(input("ingrese el monto a pagar: $"))
        if pago <= 0:
                print("ingrese un monto valido, debe ser por encima de $0")
                return saldo
        pago -= saldo
        print(f"""su saldo se actualizo
                su saldo actual es {saldo}""")
        print(f"el pago que acabo de realizar fue de ${pago}")
    except ValueError:
            print("error")
            return saldo

def transferencia(saldo):
    try:
        celular = int(input("Ingrese el telefono ppara realizar la transferencia: "))
        
        if not (celular.isdigit and len(celular) == 10):
            print ("el numero tiene mas caracteres, ingrese de nuevo")
            
        if celular <= 0:
                print("ingrese un monto valido, debe ser por encima de $0")
                return saldo
        celular -= saldo
        print(f"""su saldo se actualizo
                su saldo actual es {saldo}""")
        print(f"el pago que acabo de realizar fue de ${celular}")
    except ValueError:
            print("error")
            return saldo    

def cuenta(saldo):

    print(f"""el saldo actual de su cuenta es de 
                   ***{saldo}***""")

def main():
    opcion = 0
    saldo = 0.0
    while ((opcion != 5)):
        
        opcion = leer_opcion()

        if opcion == 1:
            cargar_saldo()
        elif opcion ==2:
            pagar()
        elif opcion ==3:
            transferencia()
        elif opcion ==4:
            cuenta()
        elif opcion ==5:
            pass
        else:
            print("\nGracias por usar el software. adios...")
            
        input("Presione cualquier tecla para continuar....")
        print("\n\n")

if __name__=="__main__":
    main()
