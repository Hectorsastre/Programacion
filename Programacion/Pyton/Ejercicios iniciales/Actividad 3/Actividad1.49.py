#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado teindique en qué posición de la palabra se encuentra la letra.
palabra_secreta=input("Introduce la palabra secreta: ")
longitud=len(palabra_secreta)
intentos=longitud
contador=0
letra=input(f"Introduce una letra: ")
for i in range(longitud):
    if letra ==palabra_secreta[i]:
        print(f"la letra existe en la posición: {i+1}")
    contador+=1
print(f"La palabra secreta era: {palabra_secreta}")