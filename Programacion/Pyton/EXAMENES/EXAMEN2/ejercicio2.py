lista=[]
lista2=[]
lista=input("Dame un enuniado:")
lista=lista.split()
palabra_buscada=input("¿Que palabra buscas? ")
posición=lista.find("palabra_buscada")
veces=lista.count(palabra_buscada)
print(f"""Lista de palabras: 
{lista}""")
