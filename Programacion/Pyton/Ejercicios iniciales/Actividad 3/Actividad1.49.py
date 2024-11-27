#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado teindique en qué posición de la palabra se encuentra la letra.
palabra_secreta=input("Introduce la palabra secreta: ")
longitud=len(palabra_secreta)
intentos=longitud
contador=0
for i in range(longitud):
    letra=input(f"Introduce una letra (intento {i+1}/{intentos}): ")
    if letra in palabra_secreta:
        print(f"la letra existe en la posición: {contador+1}")
    else:
        print("la letra no existe")
    contador=+1
print(f"La palabra secreta era: {palabra_secreta}")