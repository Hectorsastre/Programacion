# 54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural. Con While
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
    if acumulado>50:
        chivato+=1
        print(f"La suma total es: {acumulado} y el número de repeticiones es: {veces}")
        print("Programa finalizado")