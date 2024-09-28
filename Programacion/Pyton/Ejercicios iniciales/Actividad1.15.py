import math
radio=float(input("Introduce el radio del cilindro: "))
altura=float(input("Introduce la altura del cilindro: "))
area_lateral=2*math.pi*radio*altura
volumen=math.pi*(radio**2)*altura
area_lateral=round(area_lateral,2)
volumen=round(volumen,2)
print("El area lateras es de",area_lateral,"y el volumen es",volumen)
