import threading
import time

def abecedario(letra):
    for _ in range(3):
        print(letra)
        time.sleep(0.2)

for letra in "abcdefghijklm":
    hilo = threading.Thread(target=abecedario, args=(letra,))
    hilo.start()
    hilo.join()
