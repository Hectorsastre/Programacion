#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el stringdistinguiendo vocales y las consonantes:
palabra=input("Introduce una palabra: ")
vocales="aeiouAEIOU"
consonantes=""
vocales_encontradas=""
for letra in palabra:
    if letra in vocales:
        vocales_encontradas += letra
    else:
        consonantes += letra
print(f"Vocales: {vocales_encontradas}")
print(f"Consonantes: {consonantes}")