num1 = float(input("Ingresa el primer numero: "))
num2 =  float(input(" Ingresa el segundo numero"))

print("Seleccione una operacion:")
print("1.sumar")
print("2.resta")
print("3.multiplicacion")
print("4.division")

opcion = input("Elige una opcion (1-2-3-4)")

if opcion =="1":
    resultado= num1 + num2
    print("Resultado:", resultado)

elif opcion =="2":
    resultado= num1 - num2
    print("Resultado:", resultado) 

elif opcion =="3":
    resultado= num1* num2
    print("Resultado:", resultado)

elif opcion =="4":
    if num2 !=0:
        resultado = num1/num2
    print("Resultado:", resultado)
else:
    print("error: no se puede dividir entre 0")    

  


     
     
      
