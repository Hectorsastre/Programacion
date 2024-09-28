peso=float(input("Introduce tu peso en kg: "))
estatura=float(input("Introduce tu estatura en metros: "))
imc=peso/(estatura**2)
print("Tu IMC es",imc)
if imc>=25:
    print("Tienes sobrepeso")
else:
    print("Tu peso está dentro del rango normal")
