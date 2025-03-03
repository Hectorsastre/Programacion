#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir 
lista1 = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']

numeros = []
letras = []
for valor in lista1:
    if valor.isdigit():
        numeros.append(int(valor))
    else:
        letras.append(valor)

letras.sort(key=str.casefold)
numeros.sort()

orden = int(input("Introduce 1 para visualizar en orden ascendente o 2 para descendente: "))

if orden == 2:
    numeros.reverse()
    letras.reverse()

print(numeros)
print(letras)

seguir = 's'
while seguir.lower() == 's':
    eliminar = input("Introduce el valor numérico que deseas eliminar: ")
    if not eliminar.isdigit():
        print("Introduce un valor numérico")
    else:
        eliminar = int(eliminar)
        if eliminar in numeros:
            numeros.remove(eliminar)
            print(numeros + letras)
        else:
            print("El valor introducido no está en la lista")
    seguir = input("Deseas introducir otro valor s/n: ")
