#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menor a mayor.
lista=[]
aded=0
while len(lista)<4:
    aded=input("Introduce un número:")
    lista+=aded.split(",")
listaord=sorted(lista)
print(listaord)
