#inicializo valores a cada variable
var_numero=6734
var_suma=0
#obtengo su longitud
var_longitud=len(str(var_numero))#Añadir el str
#sumo cada digito a partir del índice de cada posición
var_suma = int(str(var_numero)[0]) + int(str(var_numero)[1]) + int(str(var_numero)[2]) + int(str(var_numero)[3])# Convertimos var_numero en una cadena para tener cada dígito
if var_suma % 2 == 0:  # Usamos el % para ver si es par o no
    print(f"El valor de {var_suma} es par")
else:
    print(f"El valor de {var_suma} es impar")