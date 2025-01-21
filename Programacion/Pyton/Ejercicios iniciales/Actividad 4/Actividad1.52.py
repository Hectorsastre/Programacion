#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While
chivato=0
resultado=0
while chivato==0:
    num1=int(input("Dame un numero: "))
    num2=int(input("Dame otro numero: "))
    resultado=num1+num2
    print(f"El resultado es {resultado}")
    pregunta=input("¿Quieres continuar?(responde s/n)")
    if pregunta=="n":
        chivato+=1
        print("Programa finalizado")