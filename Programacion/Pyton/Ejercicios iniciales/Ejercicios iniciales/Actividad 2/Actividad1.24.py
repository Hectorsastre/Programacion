#24. Corrige los errores del siguiente código y comprueba que se ejecuta correctamente
#cambiar las variables de 1var o 2var a var1 y var2 
var1=float(input("Introduce el peso en kg: "))
var2=float(input("Introduce la altura en metros: "))#añadir el float
var_imc=var1/var2**2#solo 1 =
print(f"Si pesas {var1} kilos y mides {var2}, tu IMC es: {var_imc}")#añadir la f al inicio del texto y rectificar las variables 
if var_imc>25:#poner:
    print("Hay sobrepeso")
else:
    print("Estás dentro de los parámetros normales")
