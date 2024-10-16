#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso(raíz y división).
import math
var=float(input("Introduce un número: "))
raiz_cuadrada=math.sqrt(var)
division=int(raiz_cuadrada/2)
print("La raíz cuadrada es",raiz_cuadrada," y la division entre 2 es",division)
