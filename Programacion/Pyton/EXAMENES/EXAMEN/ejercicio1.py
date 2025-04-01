#ejercicio1
print("****GASOLINERA****")
print("1. Sin plomo 95")
print("2. Sin plomo 98")
print("3. Gasóleo A")
print("4. Gasóleo A+")
print("*******************")
combust_elegido=int(input("Escoja el tipo de combustible: "))
valor=0
if combust_elegido==1:
    valor=1.765
if combust_elegido==2:
    valor=1.913
    descuento=10
if combust_elegido==3:
    valor=1.746
if combust_elegido==4:
    valor=1.839
    descuento=12
litros=float(input("Introduzca el número de litros que quiere respostar: "))
precio=valor*litros
if combust_elegido==2 or combust_elegido==4:
    precio_desc=precio-precio/100*descuento
    print(f"El total a pagar es {precio} y con el descuento queda en {precio_desc}")
else:
    print(f"El total a pagar es: {precio}")