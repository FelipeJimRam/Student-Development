def fixed_priority_scheduling(procesos):
    # Ordenar los procesos por prioridad
    procesos = sorted(procesos, key=lambda x: x[1], reverse=True)

    # Inicializar el tiempo de espera y el tiempo de espera promedio
    tiempo_espera = 0
    tiempo_espera_promedio = 0

    # Calcular el tiempo de espera y el tiempo de espera promedio
    for i in range(len(procesos)):
        tiempo_espera += procesos[i][2]
        tiempo_espera_promedio += procesos[i][1] + tiempo_espera

    # Calcular el tiempo de espera y el tiempo de espera promedio final
    tiempo_espera /= len(procesos)
    tiempo_espera_promedio /= len(procesos)

    # Devolver los resultados
    print(" Nombre de proceso  |  Prioridad  | Tiempo de ejecución del proceso")
    
    # Ciclo utilizado para imprimir los valores utilizados como ejemplo de manera visual con formato tabla 
    for i in range(n):
        print(" ",  procesos[i][0], "\t\t",
                    procesos[i][1], "\t\t",
                    procesos[i][2], "\t\t")
    print("El tiempo total de espera fue: ", tiempo_espera,"El tiempo de espera promedio final fue: ", tiempo_espera_promedio)

# Complemento para la impresión de los datos en formato tabla
n=3

# Datos utilizados a manera de ejemplo, para obtener el tiempo de espera del plazo fijo y el tiempo promedio de espera
if __name__ =="__main__":
    procesos = [
        ['Proceso 1', 6, 45],
        ['Proceso 2', 1, 10],
        ['Proceso 3', 2, 20],
    ]
    fixed_priority_scheduling(procesos)