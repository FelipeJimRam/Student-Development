import os
from random import randint
#Clase de Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.superior = None

    #Nos permite generar una lista aleatoria de Enteros para Apilar en nuestra Pila Vacia 
    def made_Stack(self):
        count_enter=0
        while count_enter < 20:
            datoran = randint(1,100)
            dato=datoran
            stack.apilar(dato)
            count_enter +=1

    #Nos permite apilar el dato ingresado en la parte superior
    def apilar(self, dato):
        print(f"Agregando {dato} en la cima de la pila")
        # Nos permite crear un dato si no lo hay y agregamos el valor en el elemento superior y regresamos.
        if self.superior == None:
            self.superior = Nodo(dato)
            return
        new_nodo = Nodo(dato)
        new_nodo.siguiente = self.superior
        self.superior = new_nodo

    #Nos permite desapilar y eliminar el dato superior de la Pila
    def desapilar(self):
        # Si no hay datos en el nodo superior, regresamos
        if self.superior == None:
            print("No hay ningún elemento en la pila para desapilar")
            return

        print(f"Desapilar {self.superior.dato}")
        self.superior = self.superior.siguiente

    #Nos permite revisar el último elemento que se tiene en la Pila
    def peek(self):
        print(f"El elemento superior de la Pila es: {self.superior.dato}")

    #Nos permite contar los elementos que tenemos en la Pila
    def countElements(self):
        contador = 0
        current = self.superior
        while current is not None:
            contador += 1
            current = current.siguiente
        print("Número de elementos de la Pila es de: ", contador)

    #Nos permite saber si la Pila esta vacio o no, con un Booleano
    def empty(self):
        contador = 0
        actual = self.superior
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador==0
    
    #Nos permite imprimir los datos que tengamos en la Pila
    def imprimir(self):
        print("Imprimiendo Pila...")
        # Recorremos la pila e imprimir valores
        nodo_temporal = self.superior
        while nodo_temporal != None:
            print(f"{nodo_temporal.dato}", end=",")
            nodo_temporal = nodo_temporal.siguiente
        print("")

    #Nos permite eliminar todos los datos de la Pila
    def eliminar(self):
      contador = 0
      current = self.superior
      while current is not None:
            contador += 1
            current = current.siguiente  
      
      if contador > 0:
        print("El tamaño de la Pila es: ",contador)
        contador_aux = 0 
        while contador_aux < contador:
          self.superior = self.superior.siguiente
          contador_aux += 1
      else:
        print("No hay elementos en la pila")
    #Nos permite buscar un Número x eliminando los elementos hasta encontrar el número X
    def mod_Delete(self,x):
        while x!=self.superior.dato:
           print(f"Se Desapila el número {self.superior.dato}")
           self.superior = self.superior.siguiente

def menu():
    #Función que permite limpiar las opciones y resultados obtenidos.
  os.system('cls' or 'clear') #Disclaimer: Debido a que depende del IDE,se utiliza un comando para limpiar la consola depende de ese comando para funciona correctamente
  print("!!Bienvenido al Laboratorio #2 de Pila!!")
  print("**Digite el número de la opción que desea utilizar**")
  print("\t--------------------MENÚ PRINCIPAL--------------------")
  print ("\t1 -------Crear una Pila con Lista de Enteros---------")
  print ("\t2 -------Tamaño de la Pila---------------------------")
  print ("\t3 -------Añadir Elementos a la Pila------------------")
  print ("\t4 -------Eliminar último Elemento de la Pila---------")
  print ("\t5 -------Leer elemento superior de la Pila-----------")
  print ("\t6 -------Verificar si la Pila esta Vacia-------------")
  print ("\t7 -------Eliminar todos los Elementos de la Pila-----")
  print ("\t8 -------Modificación de la Estructura--------------")
  print ("\tS --------------------Salir-------------------------")


opcionMenu="0"
#Definición de la Pila
stack=Pila()
# Inicio de la función del menu 
while opcionMenu!="S":
	# Mostramos el menu
  menu()
	# Solicitamos una opción al usuario
  opcionMenu = input("Digita una opción del menú: ")
  opcionMenu=opcionMenu.upper() #Convierte a mayúscula la entrada
  #Verificar la función de la opción 1
  if opcionMenu=="1":  #Crear una lista de Enteros con Números Aleatorios para la Pila
        print("Creando la pila...")
        stack.made_Stack()
        print("Pila Creada de forma Aleatoria!")
        input("\nPulsa cualquier tecla para continuar-->")

  #Verificar la función de la opción 2  
  elif opcionMenu=="2": #Regresar el Número de Elementos de la Pila
        stack.countElements()
        input("\nPulsa cualquier tecla para continuar-->")

  #Verificar la función de la opción 3
  elif opcionMenu=="3": #Agregar UN elemento a la Pila
        dato=int(input("Digite el Entero que quiere agregar a la Pila: "))
        stack.apilar(dato)
        stack.imprimir()
        input("\nPulsa cualquier tecla para continuar-->")

  #Verificar la función de la opción 4
  elif opcionMenu=="4": #Leer y retirar el elemento superior de la Pila
    stack.desapilar()
    stack.imprimir()
    input("\nPulsa cualquier tecla para continuar-->")

  #Verificar la función de la opción 5  
  elif opcionMenu=="5": #Leer el elemento superior de la Pila sin Retirarlo
    stack.peek()
    input("\nPulsa cualquier tecla para continuar-->")

  #Verificar la función de la opción 6  
  elif opcionMenu=="6": #Devolver 'True' si la pila esta sin elementos o 'Falso' en caso de que contenga alguno
    print("¿No hay elementos en la Pila? "+str (stack.empty()))
    input("\nPulsa cualquier tecla para continuar-->")
  
  #Verificar la función de la opción 7
  elif opcionMenu=="7": #Eliminar todos los Elementos de la Pila
    stack.eliminar()
    stack.imprimir()
    print("La Pila se ha eliminado por completo!")
    input("\nPulsa cualquier tecla para continuar-->")

  #Verificar la función de la opción 8
  elif opcionMenu=="8": #Modificación de la Estructura
    x=int(input("Digite el valor a encontrar: "))
    stack.mod_Delete(x)
    stack.imprimir()
    input("\nPulsa cualquier tecla para continuar-->")

  #Verificar la función de la opción Salir
  elif opcionMenu=="S":
    pass
  else:
    print ("")
    input("No has pulsado ninguna opción correcta...\n Pulsa cualquier tecla para continuar: ")