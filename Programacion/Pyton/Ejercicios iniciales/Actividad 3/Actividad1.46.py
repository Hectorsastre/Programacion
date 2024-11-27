#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con lapalabra Abrigo utilizando únicamente una instrucción.
palabra=input("Introduce una palabra: ")
vocales="aeiouAEIOU"
consonantes=""
vocales_encontradas=""
for letra in palabra:
    if letra in vocales:
        vocales_encontradas+=letra
    else:
        consonantes+=letra
print(f"Vocales: {vocales_encontradas}")
print(f"Consonantes: {consonantes}")