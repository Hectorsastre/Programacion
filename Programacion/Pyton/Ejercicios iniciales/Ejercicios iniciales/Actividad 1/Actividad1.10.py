var1=float(input("Dame un numero: "))
var2=float(input("Dame otro numero: "))
cociente=var1//var2
resto=var1%var2
print("El cociente es",cociente,", y el resto es",resto)
if resto==0:
    print("El dividendo es par")
else:
    print("El dividendo es impar")