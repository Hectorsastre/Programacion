#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.
precio_entrada=12
descuento_adulto=0.10
descuento_menor=0.50
num_menores=int(input("Introduce el número de menores de 18 años: "))
num_adultos=int(input("Introduce el número de adultos: "))
precio_adulto=precio_entrada*(1-descuento_adulto)
precio_menor=precio_entrada*(1-descuento_menor)
total=(num_adultos*precio_adulto)+(num_menores*precio_menor)
total_round=round(total,2)
print("El total total a pagar es de",total_round,"euros")
