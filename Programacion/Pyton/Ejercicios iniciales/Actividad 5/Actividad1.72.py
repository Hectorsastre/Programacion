#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista

vocales_a=["a","á","à","A","Á","À"]
vocales_e=["e","é","è","E","É","È"]
vocales_i=["i","í","ì","I","Í","Ì"]
vocales_o=["o","ó","ò","O","Ó","Ò"]
vocales_u=["u","ú","ù","U","Ú","Ù"]
lista=[]

repetir=input("Deseas empezar? s/n ")
while repetir=="s":
    letra=input("Introduce una letra: ")
    if letra in vocales_a:
        letra="a"
    if letra in vocales_e:
        letra="e"
    if letra in vocales_i:
        letra="i"
    if letra in vocales_o:
        letra="o"
    if letra in vocales_u:
        letra="u"
    if letra not in lista:
        lista.append(letra)
    seguir=input("Deseas continuar? s/n ")
    if seguir=="s":
        repetir="s"
    else:
        repetir="n"
print (lista)