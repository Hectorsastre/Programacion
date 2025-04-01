#ejercicio2
positivos=0
negativos=0
for i in range(6):
    num=int(input("Dame un numero: "))
    if num>=0:
        positivos+=num
    else:
        negativos+=num
print(f"Suma de numeros positivos: {positivos}")
print(f"Suma de numeros negativos: {negativos}")