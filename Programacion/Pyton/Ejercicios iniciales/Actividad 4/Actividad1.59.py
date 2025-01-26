#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe mostrarse por pantalla un mensaje y el número de intentos.
import random
numero_aleatorio=random.randint(0, 1000)
intentos=0
chiv=True
while chiv=True:
    numero_usuario=int(input("Adivina el número entre 0 y 1000: "))
    intentos+=1
    if numero_usuario<numero_aleatorio:
        print("El número es mayor. Intenta de nuevo.")
    elif numero_usuario>numero_aleatorio:
        print("El número es menor. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Adivinaste el número {numero_aleatorio}.")
        print(f"Lo lograste en {intentos} intentos.")
        chiv=False
