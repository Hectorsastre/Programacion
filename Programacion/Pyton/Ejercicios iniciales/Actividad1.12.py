#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
altura=float(input("Vamos a calcular el area y el perimetro de un trapecio isósceles, dame la altura: "))
base_mayor=float(input("Dame la base mayor: "))
base_menor=float(input("Dame la base menor: "))
lado=float(input("Dame un numero: "))
import math
perimetro=base_mayor+base_menor+2*lado
area=((base_mayor+base_menor)*altura)/2
print("El perimetro es",perimetro," y el area es",area) 
