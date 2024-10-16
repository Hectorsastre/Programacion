#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math
radio=float(input("Introduce el radio del cilindro: "))
altura=float(input("Introduce la altura del cilindro: "))
area_lateral=2*math.pi*radio*altura
volumen=math.pi*(radio**2)*altura
area_lateral=round(area_lateral,2)
volumen=round(volumen,2)
print("El area lateras es de",area_lateral,"y el volumen es",volumen)
