#40. Crea un programa que cuente todos los números pares hasta el número 50
pares=0
for numero in range(2, 51, 2):
    pares+=1
print("Hay", pares, "números pares hasta el 50.")