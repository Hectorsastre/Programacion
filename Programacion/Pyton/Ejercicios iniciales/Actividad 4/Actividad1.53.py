# 53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While
chivato=0
resultado=0
acumulado=0
veces=0
while chivato==0:
    num1=int(input("Dame un numero: "))
    num2=int(input("Dame otro numero: "))
    resultado=num1+num2
    acumulado+=resultado
    veces+=1
    print(f"El resultado es {resultado}")
    pregunta=input("¿Quieres continuar?(responde s/n): ")
    if pregunta=="n":
        chivato+=1
        print("Programa finalizado")
        print(f"La suma total es: {acumulado} y el número de repeticiones es: {veces}")