#76. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo. 
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