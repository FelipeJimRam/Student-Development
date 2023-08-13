import os
import time

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
               
    # Nos permite imprimir los elementos que tenemos en la cola como la respectiva tabla de tiempos de procesos
    def print(self):
        i=0
        print("Lista de Procesos: ")
        temp=self.head
        while temp is not None:
            print(temp.dato,end="\n")
            temp=temp.siguiente
        print("A continuación se muestran los tiempos por procesos de acuerdo a su llegada: ")
        print("Instante de Llegada | Tiempo de Servicio ")
        for i in range(n):
            print( tiempo[i][0], "\t",
                   tiempo[i][1], "\t")
    
def menu():
    #Función que permite limpiar las opciones y resultados obtenidos.
  os.system('cls' or 'clear') #Disclaimer: Debido a que depende del IDE,se utiliza un comando para limpiar la consola depende de ese comando para funciona correctamente
  print("!!Bienvenido a la Planificación tipo FCFS en Cola!!")
  print("**Digite el número de la opción que desea utilizar**")
  print("\t--------------------MENÚ PRINCIPAL--------------------")
  print ("\t1 -------Eliminar todos los Elementos de la Cola-------")  
  print ("\t2 -------Insertar Elemento al Final de la Cola---------")
  print ("\t3 -------Devolver Elemento del Frente de la Cola-------")
  print ("\t4 -------Devolver Elemento del Final de la Cola--------")
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
  if opcionMenu=="1": #Eliminar todos los elementos de la Cola
        tiempo_inicio=time.time() #Obtiene el tiempo actual
        queue.eliminar()
        tiempo_fin=time.time()   #Tiempo en que termino la ejecución
        tiempo_ejecucion=tiempo_fin - tiempo_inicio
        print("La Cola se ha eliminado por completo!")
        input("\nPulsa cualquier tecla para continuar-->")

  #Verificar la función de la opción 2
  elif opcionMenu=="2": #Insertar Elemento al final de la Cola
        n=4
        count=0
        tiempo = []
        for i in range(n):
          tiempo.append([])
          for j in range(1):
            dato=int(input("Digite el Proceso que quiere agregar a la Cola: "))
            count=count+1
            tiempo_inicio=time.time() #Obtiene el tiempo actual
            tiempo[i].append(tiempo_inicio)
            queue.enqueue(dato)
            tiempo_fin=time.time() #Tiempo en que termino la ejecución
            tiempo_pro=tiempo_fin+count
            tiempo[i].append(tiempo_pro)
        queue.print(), "\n"
        input("\nPulsa cualquier tecla para continuar-->")

  #Verificar la función de la opción 4
  elif opcionMenu=="3": #Devolver el Elemento del Frente de la Cola
        print("El elemento presente en el frente de la Cola")
        tiempo_inicio=time.time() #Obtiene el tiempo actual
        queue.front()
        tiempo_fin=time.time()   #Tiempo en que termino la ejecución
        tiempo_ejecucion=tiempo_fin - tiempo_inicio
        input("\nPulsa cualquier tecla para continuar-->")

  #Verificar la función de la opción 5  
  elif opcionMenu=="4": #Devolver el Elemento del Final de la Cola
        print("El elemento presente en el final de la Cola")
        tiempo_inicio=time.time() #Obtiene el tiempo actual
        queue.final()
        tiempo_fin=time.time()   #Tiempo en que termino la ejecución
        tiempo_ejecucion=tiempo_fin - tiempo_inicio
        input("\nPulsa cualquier tecla para continuar-->")

  
  #Verificar la función de la opción Salir
  elif opcionMenu=="S":
    pass
  else:
    print ("")
    input("No has pulsado ninguna opción correcta...\n Pulsa cualquier tecla para continuar: ")
