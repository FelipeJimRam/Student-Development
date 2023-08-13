#"\t" Es un caracter que nos permite generar un tab horizontal para poder hacer la tabla, se implementara varias veces.
#Función que nos permite definir el tiempo de espera para los procesos aquí llevados

# Función para calcular el tiempo de respuesta
def tiempoRespuesta(procesos, n, time_w, tat):
    # Calculando el tiempo de respuesta
    for i in range(n):
        tat[i] = procesos[i][1] + time_w[i]

def buscarTiempo(procesos, n, time_w):
    list_save = [0] * n
    # Copia el tiempo de ráfaga en la lista
    for i in range(n):
        list_save[i] = procesos[i][1]
    total = 0
    time = 0
    mini = 9999
    tiny = 0
    scan = False
    #Procede hasta que todos los procesos esten completos
    while (total != n):
        # Encuentra el proceso con el tiempo restante mínimo entre los procesos que llegan hasta el tiempo actual
        for c in range(n):
            if ((procesos[c][2] <= time) and
                (list_save[c] < mini) and list_save[c] > 0):
                mini = list_save[c]
                tiny = c
                scan = True
        if (scan == False):
            time += 1
            continue
             
        # Reduce el tiempo restan en 1
        list_save[tiny] -= 1
 
        # Actualiza el minimo
        mini = list_save[tiny]
        if (mini == 0):
            mini = 9999
 
        # Si el proceso se completa se ejecuta
        if (list_save[tiny] == 0):
 
            # Incremento completado
            total += 1
            scan = False
 
            # Buscar la hora de finalización del proceso actual
            final_time = time + 1
 
            # Calcula el tiempo de espera
            time_w[tiny] = (final_time - proc[tiny][1] -   
                                proc[tiny][2])
 
            if (time_w[tiny] < 0):
                time_w[tiny] = 0
         
        # Incremento del tiempo
        time += 1
 
# Función para calcular tiempos medios de espera y respuesta.
def tiempoPromedio(procesos, n):
    time_w = [0] * n
    tat = [0] * n
 
    # Función para encontrar el tiempo de espera de todos los procesos
    buscarTiempo(procesos, n, time_w)
 
    # Función para encontrar el tiempo de respuesta para todos los procesos
    tiempoRespuesta(procesos, n, time_w, tat)
 
    # Muestra los procesos junto con todos los detalles
    print(" Procesos   |   Ráfaga   |  Tiempo de Espera | Tiempo de Respuesta |")
    total_time_w = 0
    total_tat = 0
    #Nos permite imprimir la lista
    for i in range(n):
        total_time_w = total_time_w + time_w[i]
        total_tat = total_tat + tat[i]
        print(" ", procesos[i][0], "\t\t",
                   procesos[i][1], "\t\t",
                   time_w[i], "\t\t", tat[i])
 
    print("El Tiempo de espera Promedio: %.5f "%(total_time_w /n) )
    print("El Tiempo de respuesta promedio: ", total_tat /n)
     
#Código principal de SFJ
if __name__ =="__main__":
    print("!!Bienvenido a la Planificación tipo SJF!!")
    #En este apartado del código nos permite almacenar los datos ingresados para luego procesarlos en las funciones mediante sublistas
    n = 5
    proc = []
    for i in range(5):
        proc.append([])
        for j in range(1):
            num_Id=int(input("Ingrese el número de ID: "))
            proc[i].append(num_Id)
            num_Rafa=int(input("Ingrese el número de Rafaga: "))
            proc[i].append(num_Rafa)
            num_Llega=int(input("Ingrese el Tiempo de Llegada: "))
            proc[i].append(num_Llega)
    tiempoPromedio(proc, n)