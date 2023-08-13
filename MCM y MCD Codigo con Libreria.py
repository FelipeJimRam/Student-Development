import math
#Prerequisito! Es necesario contar con la versión de Python 3.9 para compilar

print ("---------------Bienvenido a calculadora para M.C.M y M.C.D------------------")
#Inicio de Función para hallar el MCM por medio de listas y de Math
def minimocm():
    cantidad = int(input("Digite la cantidad de números que desea ingresar: "))
    print(f"Solicitare {cantidad} números:")
    numeros = []
    for i in range(cantidad):
        numero = input(f"Ingresa el número {i + 1}: ")
        numero = int(numero)
        numeros.append(numero)
#Condicional para saber el número ingresado por el usuario e ingresar a la operación
    if len(numeros)==2:
        print(math.lcm(numeros[0],numeros[1]))
        menu()

    elif len(numeros)==3:
        print("El M.C.M es:", math.lcm(numeros[0],numeros[1],numeros[2]))
        menu()

    elif len(numeros)==4:
        print("El M.C.M es:", math.lcm(numeros[0],numeros[1],numeros[2],numeros[3]))
        menu()

    elif len(numeros)==5:
        print("El M.C.M es:", math.lcm(numeros[0],numeros[1],numeros[2],numeros[3],numeros[4]))
        menu()

    elif len(numeros)==6:
        print("El M.C.M es:", math.lcm(numeros[0],numeros[1],numeros[2],numeros[3],numeros[4],numeros[5]))
        menu()

    elif len(numeros)==7:
        print("El M.C.M es:", math.lcm(numeros[0],numeros[1],numeros[2],numeros[3],numeros[4],numeros[5],numeros[6]))
        menu()

    elif len(numeros)==8:
        print("El M.C.M es:", math.lcm(numeros[0],numeros[1],numeros[2],numeros[3],numeros[4],numeros[5],numeros[6],numeros[7]))
        menu()

    elif len(numeros)==9:
        print("El M.C.M es:", math.lcm(numeros[0],numeros[1],numeros[2],numeros[3],numeros[4],numeros[5],numeros[6],numeros[7],numeros[8]))
        menu()
    
    elif len(numeros)==10:
        print("El M.C.M es:", math.lcm(numeros[0],numeros[1],numeros[2],numeros[3],numeros[4],numeros[5],numeros[6],numeros[7],numeros[8],numeros[9]))
        menu()
#Inicio de Función para hallar el MCD por medio de listas y de Math
def maximocd():
    cantidad = int(input("Digite la cantidad de números que desea ingresar: "))
    print(f"Solicitare {cantidad} números:")
    numeros = []
    for i in range(cantidad):
        numero = input(f"Ingresa el número {i + 1}: ")
        numero = int(numero)
        numeros.append(numero)
#Condicional para saber el número ingresado por el usuario e ingresar a la operación
    if len(numeros)==2:
        print(math.gcd(numeros[0],numeros[1]))
        menu()

    elif len(numeros)==3:
        print("El M.C.D es:", math.gcd(numeros[0],numeros[1],numeros[2]))
        menu()

    elif len(numeros)==4:
        print("El M.C.D es:", math.gcd(numeros[0],numeros[1],numeros[2],numeros[3]))
        menu()

    elif len(numeros)==5:
        print("El M.C.D es:", math.gcd(numeros[0],numeros[1],numeros[2],numeros[3],numeros[4]))
        menu()

    elif len(numeros)==6:
        print("El M.C.D es:", math.gcd(numeros[0],numeros[1],numeros[2],numeros[3],numeros[4],numeros[5]))
        menu()

    elif len(numeros)==7:
        print("El M.C.D es:", math.gcd(numeros[0],numeros[1],numeros[2],numeros[3],numeros[4],numeros[5],numeros[6]))
        menu()

    elif len(numeros)==8:
        print("El M.C.D es:", math.gcd(numeros[0],numeros[1],numeros[2],numeros[3],numeros[4],numeros[5],numeros[6],numeros[7]))
        menu()

    elif len(numeros)==9:
        print("El M.C.D es:", math.gcd(numeros[0],numeros[1],numeros[2],numeros[3],numeros[4],numeros[5],numeros[6],numeros[7],numeros[8]))
        menu()

    elif len(numeros)==10:
        print("El M.C.D es:", math.gcd(numeros[0],numeros[1],numeros[2],numeros[3],numeros[4],numeros[5],numeros[6],numeros[7],numeros[8],numeros[9]))
        menu()
#Inicio de función con la que se abre un menú para que el usuario elija la operación a realizar
def menu():
    print("!!Recuerde: Debe ingresar un mínimo de 2 números y hasta un máximo de 10 números!!")
    print("**Digite el número de la opción que desea utilizar**")
    print("--------MENÚ PRINCIPAL--------")
    print("---1.Mínimo Común Múltiplo---")
    print("---2.Máximo Común Divisor---")
    print("---------3.Salir----------")
    return int(input())

op=menu()

while op>=1 and op<3 :
    if op==1:
        minimocm()
    elif op==2:
        maximocd()
    if op >=3:
       print ("Salir")
       break