#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.
inicio= int(input("Introduce el primer número: "))
fin= int(input("Introduce el segundo número: "))

if inicio>fin:
    inicio, fin=fin, inicio
numero=inicio

while numero<=fin:
    if numero%2==0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")
    numero+=1