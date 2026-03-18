import  threading
import time

def tarea(numero):
    print(f"numero de hilo{numero}")
    

inicio = time.perf_counter()

hilos = []

for i in range(1,100):
    hilo =  threading. Thread(target= tarea, args=(i,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo. join()    

Fin = time.perf_counter()    


tiempo = Fin - inicio

