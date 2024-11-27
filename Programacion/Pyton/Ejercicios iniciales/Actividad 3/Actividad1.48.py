#48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud deesa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuariotenga x oportunidades para ver si letra introducida está en esa palabra.
palabra_secreta=input("Introduce la palabra secreta: ")
longitud=len(palabra_secreta)
intentos=longitud
for i in range(intentos):
    letra=input(f"Introduce una letra (intento {i+1}/{intentos}): ")
    if letra in palabra_secreta:
        print(f"la letra existe")
    else:
        print("la letra no existe")
print(f"La palabra secreta era: {palabra_secreta}")