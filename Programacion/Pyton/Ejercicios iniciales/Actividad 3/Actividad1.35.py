#35. Programa que al introducir un número por teclado permita mostrar ese número de veces tu nombre
nombre=("Héctor Sastre")
numero_repeticiones=int(input("¿Cuántas veces quieres que se muestre tu nombre? "))
for repetir in range(numero_repeticiones):
    print(nombre)