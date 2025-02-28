#84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra. 
import random
listapalabras=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
listaletras=[]
listadesorden=[]
palabra=random.choice(listapalabras)
for recorrer in palabra:
    listaletras.append(recorrer)
while len(listaletras)>0:
    letra=random.choice(listaletras)
    listadesorden.append(letra)
    listaletras.remove(letra)
palabradesorden="".join(listadesorden)

print(f"Adivina la palabra oculta:",listadesorden)
usuario=input("Introduce tu respuesta: ")

while usuario!=palabra:
    print("Error, no es correcta")
    usuario=input("Introduce otra palabra: ")
else:
    print("Correcto")

