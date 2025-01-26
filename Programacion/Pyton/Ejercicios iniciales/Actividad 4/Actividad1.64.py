#64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
pares=0
impares=0
positivos=0
negativos=0
ceros=0
suma=0
numero=0

while numero!=-99:
    numero=int(input("Introduce un número (-99 para terminar): "))
    if numero!=-99:
        suma+=numero
        if numero==0:
            ceros+=1
        elif numero>0:
            positivos+=1
        else:
            negativos+=1
        if numero%2==0:
            pares+=1
        else:
            impares+=1
print("RESUMEN")
print(f"Total de pares: {pares}")
print(f"Total de impares: {impares}")
print(f"Total de positivos: {positivos}")
print(f"Total de negativos: {negativos}")
print(f"Total de ceros: {ceros}")
print(f"Suma total: {suma}")
