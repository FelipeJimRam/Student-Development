
print ("---Bienvenido a calculadora para M.C.M y M.C.D---")
#Se inicia una función que nos permite realizar el MCM por medio de bucles y de condionales.
def minimocm():

    if numcalculo==2:
        n1=int(input("Digite el número: "))
        n2=int(input("Digite el número: "))

        i=2
        while True:
            if i%n1==0 and i%n2==0:
                mcm=i

                break
                
            i+=1
        print (f"El MCD de {n1} y {n2} es: {mcm}")
        menu()

    elif numcalculo==3:
        n1=int(input("Digite el número: "))
        n2=int(input("Digite el número: "))
        n3=int(input("Digite el número: "))

        i=2
        while True:
            if i%n1==0 and i%n2==0 and i%n3==0:
                mcm=i

                break
                
            i+=1
        print (f"El MCD de {n1} , {n2} y {n3} es: {mcm}")
        menu()

    elif numcalculo==4:
        n1=int(input("Digite el número: "))
        n2=int(input("Digite el número: "))
        n3=int(input("Digite el número: "))
        n4=int(input("Digite el número: "))

        i=2
        while True:
            if i%n1==0 and i%n2==0 and i%n3==0 and i%n4==0:
                mcm=i

                break
                
            i+=1
        print (f"El MCD de {n1} , {n2} , {n3} y {n4} es: {mcm}")
        menu()

    elif numcalculo==5:
        n1=int(input("Digite el número: "))
        n2=int(input("Digite el número: "))
        n3=int(input("Digite el número: "))
        n4=int(input("Digite el número: "))
        n5=int(input("Digite el número: "))

        i=2
        while True:
            if i%n1==0 and i%n2==0 and i%n3==0 and i%n4==0 and i%n5==0:
                mcm=i

                break
                
            i+=1
        print (f"El MCD de {n1} , {n2} , {n3} , {n4} y {n5} es: {mcm}")
        menu()
#Se inicia una función que nos permite realizar el MCD por medio de bucles y de condionales.
def maximocd():

    if numcalculo==2:
        n1= int(input("Digite un número: "))
        n2= int(input("Digite un número: "))

        i = 1
        mcd = 0
        while (i <= 100):
            if ((n1 % i == 0) and (n2 % i == 0)):
                if (i > mcd):
                        mcd = i
            i = i + 1

        print(f"El MCD de {n1} y {n2} es: {mcd}")
        menu()

    elif numcalculo==3:
        n1= int(input("Digite un número: "))
        n2= int(input("Digite un número: "))
        n3= int(input("Digite un número: "))

        i = 1
        mcd = 0
        while (i <= 100):
            if ((n1 % i == 0) and (n2 % i == 0) and (n3 % i == 0)):
                if (i > mcd):
                        mcd = i
            i = i + 1

        print(f"El MCD de {n1} , {n2} y {n3} es: {mcd}")
        menu()

    elif numcalculo==4:
        n1= int(input("Digite un número: "))
        n2= int(input("Digite un número: "))
        n3= int(input("Digite un número: "))
        n4= int(input("Digite un número: "))

        i = 1
        mcd = 0
        while (i <= 100):
            if ((n1 % i == 0) and (n2 % i == 0) and (n3 % i == 0) and (n4 % i == 0)):
                if (i > mcd):
                        mcd = i
            i = i + 1

        print(f"El MCD de {n1} , {n2} , {n3} y {n4} es: {mcd}")
        menu()

    elif numcalculo==5:
        n1= int(input("Digite un número: "))
        n2= int(input("Digite un número: "))
        n3= int(input("Digite un número: "))
        n4= int(input("Digite un número: "))
        n5= int(input("Digite un número: "))

        i = 1
        mcd = 0
        while (i <= 100):
            if ((n1 % i == 0) and (n2 % i == 0) and (n3 % i == 0) and (n4 % i == 0)):
                if (i > mcd):
                        mcd = i
            i = i + 1

        print(f"El MCD de {n1} , {n2} , {n3} , {n4} y {n5} es: {mcd}")  
        menu() 
#Se inicia una función que nos permite abrirle al usuario un menú por el cuál podra elegir la operación a realizar y la cantidad de números que validara.
def menu():
    print("!!Recuerde: Debe ingresar un mínimo de 2 números y hasta un máximo de 10 números!!")
    print("**Digite el número de la opción que desea utilizar**")
    print("-------MENÚ PRINCIPAL-------")
    print("---1.Mínimo Común Múltiplo---")
    print("---2.Máximo Común Divisor---")
    print("----------3.Salir---------")
    return int(input())

op=menu()

while op>=1 and op<3 :
    if op==1:
        numcalculo=int(input("¿Cúantos números desea ingresar para hacer la operación? "))
        minimocm()
    elif op==2:
        numcalculo=int(input("¿Cúantos números desea ingresar para hacer la operación? "))
        maximocd()
    elif op>=3:
       print ("Salir")
       break
