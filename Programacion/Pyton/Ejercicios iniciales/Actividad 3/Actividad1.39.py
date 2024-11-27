#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.
numero=int(input("Introduce la cantidad de números: "))
positivos=0
negativos=0
ceros=0
for a in range(numero):
    numero = int(input(f"Introduce el número {a+1}: "))
    if numero>0:
        positivos+=1
    elif numero<0:
        negativos+=1
    else:
        ceros+=1
print(f"La cantidad de números positivos: {positivos}, la cantidad de números negativos: {negativos} y la cantidad de números ceros: {ceros}")