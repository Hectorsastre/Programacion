#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
numero_aleatorio = random.randint(1, 5)
chiv=True
acumulado=0
while chiv=True or acumulado==3:
    numero_usuario=input("Adivina el número entre 1 y 5: ")
    
    if numero_usuario.isdigit():
        numero_usuario=int(numero_usuario)
        
        if 1<=numero_usuario<=5:
            if numero_usuario==numero_aleatorio:
                print("¡Felicidades! Adivinaste el número.")
                continuar=input("¿Quieres intentarlo de nuevo? (sí/no): ").lower()
                if continuar!="sí":
                    print("¡Hasta luego!")
                    chiv=False
            else:
                print("Intenta nuevamente.")
                acumulado+=1
        else:
            print("Por favor, introduce un número entre 1 y 5.")
    else:
        print("Por favor, introduce un número válido.")