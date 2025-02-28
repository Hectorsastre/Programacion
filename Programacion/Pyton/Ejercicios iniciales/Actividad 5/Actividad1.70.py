#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo.
lista1=[]
cantidad_palabras=int(input("introduce la cantidad de palabras: "))
for i in range(cantidad_palabras):
    palabra=input(f"Introduce {i+1}ª palabra: ")
    lista1.append(palabra)
lista2=lista1.copy()
lista1.sort()
lista2.sort(reverse=True)
print(f"lista1 contiene: {lista1}")
print(f"lista2: contiene {lista2}")
