def menu():
    print("""*** CALCULADORA SENCILLA ***
1. Registrar estudiante
2. Asignar notas parciales
3. Registrar numero de inasistencia
4. Mostrar datos del estudiante
5. Calcular nota final
6. Salir
----------------
Opción?(1-6): """)
    
def leer_opcion():
    menu()
    op = input()
    while(not op.isdigit() or int(op)<1 or int(op)>6):
        print("Opción no válida, digite un número del 1 al 6: ")
        input("Presione cualquier tecla para continuar...")
        print("\n\n")
        menu()
        op = input()

    return int(op)
    
def registrar_estudiante():
    print("\n\n\n*** 1. Registrar estudiante")
    cod = input("Código del estudiante")
    nom = input("Nombre del estudiante")
    return cod,nom

def leer_notas():
    print("\n\n\n*** 2. Leer notas parciales ")
    n1 = float(input("Parcial 1: "))
    n2 = float(input("Parcial 2: "))
    n3 = float(input("Parcial 3: "))
    
    return n1,n2,n3

def inasistencias():
    print("\n\n\n*** 3. Numero de inasistencias")
    ina = int(input("Número de inasistencias: "))
  
    return ina

def mostrar_datos(codigo, nombre, n1, n2, n3, num_inasistencias):
    print("\n\n\n*** 4.Datos del estudiante")
    print("* Codigo: ", codigo)
    print("* Nombre: ", nombre)
    print("* Nota 1: ",n1)
    print("* Nota 2: ",n2)
    print("* Nota 3: ",n3)
    print("* Num Inasistencias: ",num_inasistencias)

def calcular_nota_final(cod, nom, n1, n2, n3, num_inasistencias):
    print("\n\n\n*** 5.Nota final")

    prom=(n1+n2+n3) / 3
    if 10 <= num_inasistencias < 15:
        prom -=0.5
    elif num_inasistencias >= 15:
        prom -=1
        print("COD\tNOMBRE\t\t\tP1\t\P2\tP3\tINASISTENCIAS\tNOTA FINAL")
        print(f"{cod}\t{nom}\t\t\t{n1}\t{n2}\t{n3}\t{num_inasistencias}\t{prom}")


def main():
    opcion = 0
    nombre = ""
    codigo = ""
    n1 = 0
    n2 = 0
    n3 = 0
    num_inasistencias = 0
    nota_final = 0
    while ((opcion != 6)):
        
        opcion = leer_opcion()

        if opcion == 1:
            codigo,nombre 
            registrar_estudiante()
        elif opcion ==2:
            n1, n2, n3 
            leer_notas()
        elif opcion ==3:
            num_inasistencias 
            inasistencias()
        elif opcion ==4:
            mostrar_datos()
        elif opcion ==5:
            calcular_nota_final(codigo, nombre, n1, n2, n3, nota_final)
        else:
            print("\nGracias por usar el software. adios...")
            
        input("Presione cualquier tecla para continuar....")
        print("\n\n")

main()