#7. programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?
import math
var1=float(input("Dame un numero: "))
var2=float(input("Dame otro numero: "))
suma=var1+var2
resta=var1-var2
multiplicacion=var1*var2
#para redondear a 2 decimales, usa round(x,2)#
division=var1/var2
exponente=var1**var2
division_entera=var1//var2
print("La suma es: ",suma)
print("La resta es: ",resta)
print("La multiplicación es: ",multiplicacion)
print("La división redondeada a dos decimales es: ",round(division,2))
print("El resultado del primer numero con exponente del segundo es: ",exponente)
print("Finalmente, la división entera es: ",division_entera)
