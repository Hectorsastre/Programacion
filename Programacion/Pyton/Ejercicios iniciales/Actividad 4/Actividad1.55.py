# 55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
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
    print(f"El total acumulado es: {acumulado} y llevas {veces} operación/es realizada")
    if not acumulado<50 and acumulado%2==0:
        chivato+=1
        print(f"La suma total es: {acumulado} y el número de repeticiones es: {veces}")
        print("Programa finalizado")