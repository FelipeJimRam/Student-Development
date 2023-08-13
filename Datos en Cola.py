import os
from random import randint

#Clase de Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior= None

class Cola:
    def __init__(self):
        self.head=None
        self.last=None

    #Nos permite generar una lista aleatoria de Enteros para Apilar en nuestra Pila Vacia 
    def made_Queue(self):
        count_enter=0
        while count_enter < 20:
            datoran = randint(1,100)
            dato=datoran
            queue.enqueue(dato)
            count_enter +=1

    #Nos permite Encolar el dato ingresado en la parte Inferior
    def enqueue(self, dato):
        print(f"Agregando {dato} en el Final de la Cola")
        if self.last is None:
            self.head =Nodo(dato)
            self.last =self.head
        else:
            self.last.siguiente = Nodo(dato)
            self.last.siguiente.anterior=self.last
            self.last = self.last.siguiente

    #Nos permite remover el primer elemento y retornar el elemento de la Cola
    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp= self.head.dato
            print ("Desencolando...")
            print(f"El elemento Desencolado fue: {self.head.dato}")
            self.head = self.head.siguiente
            self.head.anterior=None
            return temp

    #Nos permite ver el elemento del frente de la Cola
    def front(self):
        print(f"Elemento: {self.head.dato}")
   
    #Nos permite ver el elemento del final de la Cola
    def final(self):
        print(f"Elemento: {self.last.dato}")

    #Nos permite saber si la Cola esta vacio o no, con un Booleano  
    def empty(self):
        if self.head is None:
            return True
        else:
            return False
    
    #Función que elimina todos los elementos que existen en la Cola y la deja vacía
    def eliminar(self):
      temp=self.head
      count=0
      while temp is not None:
            count=count+1
            temp=temp.siguiente
  
      if count > 0:
        print("El tamaño de la Cola es: ",count)
        count_aux = 0 
        while count_aux < count:
          print(f"Eliminar cola {self.head.dato}")
          self.head = self.head.siguiente
          count_aux += 1
      else:
        print("No hay elementos en la cola")
               
    # Nos permite imprimir los elementos que tenemos en la cola
    def print(self):
        print("Los elementos de la Cola son: ")
        temp=self.head
        while temp is not None:
            print(temp.dato,end="->")
            temp=temp.siguiente
    
    #Nos permite buscar un Número x eliminando los elementos hasta encontrar el número X
    def mod_Delete(self,x):
        while x!=self.head.dato:
           print(f"Se Desapila el número {self.head.dato}")
           self.head = self.head.siguiente
           self.head.anterior=None
    

def menu():
    #Función que permite limpiar las opciones y resultados obtenidos.
  os.system('cls' or 'clear') #Disclaimer: Debido a que depende del IDE,se utiliza un comando para limpiar la consola depende de ese comando para funciona correctamente
  print("!!Bienvenido al Laboratorio #2 de Cola!!")
  print("**Digite el número de la opción que desea utilizar**")
  print("\t--------------------MENÚ PRINCIPAL--------------------")
  print ("\t1 -------Crear una Cola con Lista de Enteros-----------")
  print ("\t2 -------Eliminar todos los Elementos de la Cola-------")
  print ("\t3 -------Verificar si la Cola esta Vacia---------------")
  print ("\t4 -------Devolver Elemento del Frente de la Cola-------")
  print ("\t5 -------Devolver Elemento del Final de la Cola--------")
  print ("\t6 -------Remover Elemento del frente de la Cola--------")
  print ("\t7 -------Insertar Elemento al Final de la Cola---------")
  print ("\t8 -------Modificación de la Estructura-----------------")
  print ("\tS --------------------Salir-----------------------")


opcionMenu="0"
#Definición de la Cola
queue=Cola()
# Inicio de la función del menu 
while opcionMenu!="S":
	# Mostramos el menu
  menu()
	# Solicitamos una opción al usuario
  opcionMenu = input("Digita una opción del menú: ")
  opcionMenu=opcionMenu.upper() #Convierte a mayúscula la entrada
  #Verificar la función de la opción 1
  if opcionMenu=="1":  #Crear una lista de Enteros con Números Aleatorios para la Cola
        print("Creando la Cola...")
        queue.made_Queue()
        print("Cola Creada de forma Aleatoria!")
        input("\nPulsa cualquier tecla para continuar-->")

  #Verificar la función de la opción 2  
  elif opcionMenu=="2": #Eliminar todos los elementos de la Cola
        queue.eliminar()
        print("La Cola se ha eliminado por completo!")
        input("\nPulsa cualquier tecla para continuar-->")


  #Verificar la función de la opción 3
  elif opcionMenu=="3": #Devolver 'True' si la cola esta sin elementos o 'Falso' en caso de que contenga alguno
        print("¿No hay elementos en la Cola? "+str (queue.empty()))
        input("\nPulsa cualquier tecla para continuar-->")

  #Verificar la función de la opción 4
  elif opcionMenu=="4": #Devolver el Elemento del Frente de la Cola
        print("El elemento presente en el frente de la Cola")
        queue.front()
        input("\nPulsa cualquier tecla para continuar-->")

  #Verificar la función de la opción 5  
  elif opcionMenu=="5": #Devolver el Elemento del Final de la Cola
        print("El elemento presente en el final de la Cola")
        queue.final()
        input("\nPulsa cualquier tecla para continuar-->")

  #Verificar la función de la opción 6  
  elif opcionMenu=="6": #Devolver 'True' si la pila esta sin elementos o 'Falso' en caso de que contenga alguno
        queue.dequeue()
        input("\nPulsa cualquier tecla para continuar-->")
  
  #Verificar la función de la opción 7
  elif opcionMenu=="7": #Insertar Elemento al final de la Cola
        dato=int(input("Digite el Entero que quiere agregar a la Cola: "))
        queue.enqueue(dato)
        queue.print()
        input("\nPulsa cualquier tecla para continuar-->")

  #Verificar la función de la opción 8
  elif opcionMenu=="8": #Modificación de la Estructura
        x=int(input("Digite el valor a encontrar: "))
        queue.mod_Delete(x)
        queue.print()
        input("\nPulsa cualquier tecla para continuar-->")

  #Verificar la función de la opción Salir
  elif opcionMenu=="S":
    pass
  else:
    print ("")
    input("No has pulsado ninguna opción correcta...\n Pulsa cualquier tecla para continuar: ")