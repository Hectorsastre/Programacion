#81. A partir de una lista definida, busca el método apropiado para que se visualice un valor de la lista al azar.
import random
listapalabras=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
palabra=random.choice(listapalabras)
print(palabra)