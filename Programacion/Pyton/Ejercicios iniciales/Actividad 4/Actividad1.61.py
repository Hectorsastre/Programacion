#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es superior o igual a 40.
numero=int(input("Introduce un número: "))
contador=1

while contador<=10 and numero*contador<40:
    print(f"{numero} x {contador}={numero*contador}")
    contador+=1
