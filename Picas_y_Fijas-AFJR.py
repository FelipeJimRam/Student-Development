import random

digitos = 0
jugar = True
gano = False
digitos= 4
intentos = 12

print ("-"*60)
print ("------------Bienvenido al Juego de Picas y Fijas------------")
print ("-"*60)

#Esta función nos permite crear el número de cuatro digitos aleatorio, iniciando así el juego de Picas y Fijas. 
def randomizador(digitos):
    aleatorio =[]
    for i in range (digitos):
        x= random.randint(1,9)
        while x in aleatorio:
            x=random.randint(1,9)
        aleatorio.append(x)
    return aleatorio

aleatorio=randomizador(digitos)

#Esta función nos permite tomar el número ingresado por el jugador cuantas veces sea necesario hasta adivinar el número del sistema
def tomarNumero(digitos):
    numero= []
    while len(numero)!=digitos:
        numero = [int(x)for x in input("Ingrese un número de "+str(digitos)+" digitos: ")]
    return numero

#Este fragmento de código se encarga de interactuar con el contador, y de comparar los digitos introducidos por el jugador
while jugar:
    numero= []
    picas= 0
    fijas= 0
    numero=tomarNumero(digitos)
    intentos-=1
    if numero ==aleatorio:
        gano= True
        jugar= False
    else:
        for n in range (digitos):
            if numero[n] in aleatorio:
                if numero [n]==aleatorio[n]:
                    fijas+=1
                else:
                    picas+=1
        print("Fijas = " +str(fijas)+" --- "+"Picas = "+str(picas)+" --- "+" Restan ("+str(intentos)+") Intentos")
        if intentos==0:
            jugar=False

#Por último este fragmento se encarga de revisar si el jugador en los intentos brindados logro o no acertar el número 
if gano:
    if intentos<=4:
        print ("Bien, Regular")
    elif intentos<=8:
        print ("Bien, Aceptable")
    elif intentos<=12:
        print("Bien, Excelente")
else:
    print("Mal, este juego como que no es para ti")
