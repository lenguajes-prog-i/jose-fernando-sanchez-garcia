import threading
import time

def programar():
    print("Inicio 1")
    time.sleep(4)
    print("Finalizo 1")

def tomaragua():
    print("Inicio 2")
    time.sleep(6)
    print("Finalizo 2")

def estudiar():
    print("Inicio 3")
    time.sleep(4)
    print("Finalizo 3")

inicio = time.perf_counter()

#programar()
#tomaragua()
#estudiar()

hilo_programar = threading.Thread(target= programar, args=())
hilo_programar. start()
hilo_tomaragua = threading.Thread(target= tomaragua, args=())
hilo_tomaragua. start()
hilo_estudiar = threading.Thread(target= estudiar, args=())
hilo_estudiar. start()

hilo_programar.join()
hilo_tomaragua.join()
hilo_estudiar.join()


Fin = time.perf_counter()

tiempo = Fin - inicio
print(tiempo)

print(threading.active_count())
print(threading.enumerate())

