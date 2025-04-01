lista=[]
lista3=[]
lista=input("Introduce 6 numeros separados por -: ")
lista=lista.split('-')
lista1=[int(x) for x in lista]
listam=max(lista1)
listamin=min(lista1)
promedio=sum(lista1)//6
print(f"Máximo: {listam}")
print(f"Mínimo: {listamin}")
print(f"Promedio: {promedio}")
for recorrer in lista1:
    if recorrer>promedio:
        lista3.append(recorrer)