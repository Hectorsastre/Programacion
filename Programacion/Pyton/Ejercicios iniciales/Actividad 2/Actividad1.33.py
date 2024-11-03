#33. Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años
frase = "No hay mal que dure cien años"
frase = frase.lower()
cantidad_a = frase.count('a')
cantidad_e = frase.count('e')
cantidad_i = frase.count('i')
cantidad_o = frase.count('o')
cantidad_u = frase.count('u')
print(f"En la frase, el numero de a es {cantidad_a} , el de e es {cantidad_e}, el de i es {cantidad_i}, el de o es {cantidad_o} y el numero de u es {cantidad_u}")