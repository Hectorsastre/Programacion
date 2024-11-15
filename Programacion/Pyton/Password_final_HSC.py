import string 
print("La longitud del password té que tenir una longitud d’entre 6 i 8 caràcters")
print("Posició 1: Un numero major o igual 1 i menor o igual que 5")
print("Posició 2: Una lletra minúscula")
print("Posició 3: Una lletra majúscula")
print("Posició 4: Un dels seguents simbols *,_ @")
print("Posicio 5: Una lletra minúscula")
print("Posició 6: Un numero major o igual 6 i menor o igual que 9")
print("Posició 7: Un dels seguents simbols &,/,#")
print("Posició 8: Un número menor o igual que 5")

Err=""
incorrecto=False
password= input("Tria una contrasenya: ")
L=len(password)
if L>8 or L<6: #el if es un condicional que devuelve positivo si la condicion posterior se cumple
    print(f"Error, el password te una longitud de {len(password)} caràcters i no compleix els requisits")
    incorrecto=True
else:
    if not password[0].isnumeric or int(password[0])<1 or int(password[0])>5:#El int lo transforma en un numero, y el isnumerico comprueva que es un numero, para que no pete si no ponen un numero
        Err=Err+("Error en el caràcter 1 ")
        incorrecto=True #modificamos la variable para activar el chivato
    if not password[1].islower():# el if not hace que si no cumple estos parametros salga un chivato positivo, que activa el condicional y printea la frase
        Err=Err+("Error en el caràcter 2 ")
        incorrecto=True
    if not password[2].isupper():
        Err=Err+("Error en el caràcter 3 ")
        incorrecto=True
    if password[3] not in "*_@":
        Err=Err+("Error en el caràcter 4 ")
        incorrecto=True
    if not password[4].islower():
        Err=Err+("Error en el caràcter 5 ")
        incorrecto=True
    if password[5] not in "6789":
        Err=Err+("Error en el caràcter 6 ")
        incorrecto=True
    if L>6:
        if password[6] not in"&/#":#si no esta en dentro de ese parametro, sale el print
            Err=Err+("Error en el caràcter 7 ")
            incorrecto=True
        if L>7:
            if not password[7].isnumeric or int(password[7])>5:
               Err=Err+("Error en el caràcter 8 ")
               incorrecto=True
if incorrecto==False:
    print("El format del PASSWORD és correcte")
else:
    print(Err)
    