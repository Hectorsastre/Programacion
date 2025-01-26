#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5
numero_aleatorio = random.randint(1, 5)
chiv=True
while chiv=True:
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
        else:
            print("Por favor, introduce un número entre 1 y 5.")
    else:
        print("Por favor, introduce un número válido.")