altura=float(input("Vamos a calcular el area y el perimetro de un trapecio isósceles, dame la altura: "))
base_mayor=float(input("Dame la base mayor: "))
base_menor=float(input("Dame la base menor: "))
lado=float(input("Dame un numero: "))
import math
perimetro=base_mayor+base_menor+2*lado
area=((base_mayor+base_menor)*altura)/2
print("El perimetro es",perimetro," y el area es",area) 
