#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número de veces que se repite cada número.
import random
contador=[0, 0, 0, 0, 0, 0]
tiros=0

while tiros<100:
    dado=random.randint(1, 6)
    contador[dado - 1]+=1
    tiros+=1

for i in range(6):
    print(f"Número {i+1}: {contador[i]} veces")

