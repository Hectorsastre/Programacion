#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la realización de un pedido, si quiere gestionar otro. 
print("""MENÚ
1. Bocadillo de calamares- 9€
2. Bocadillo de chistorra - 4.5€
3. Bikini de jamón - 2.5€

ACOMPAÑAMIENTO
1. Patatas finas - 1.5€
2. Patatas gruesas - 1.75€
3. Patatas rústicas - 2€

BEBIDAS
1. Coca cola - 2€
print("2. Acuarius - 1.5€
print("3. Agua - 1€""")
chivato=0
resultado=0
acumulado=0
veces=0
acumulado_iva=0
acumulado_final=0
repeticion=""
while chivato==0:
    menu_num=0
    acompañamiento_num=0
    bebida_num=0
    menu=0
    acompañamiento=0
    bebida=0
    menu_num=int(input("Dame el bocadillo: (1~3) "))
    if menu_num==1:
        menu+=9
    if menu_num==2:
        menu+=4.5
    if menu_num==3:
        menu+=2.5
    acompañamiento_num=int(input("Dame el acompañamiento: (1~3) "))
    if acompañamiento_num==1:
        acompañamiento+=1.5
    if acompañamiento_num==2:
        acompañamiento+=1.75
    if acompañamiento_num==3:
        acompañamiento+=2
    bebida_num=int(input("Dame la bebida: (1~3) "))
    if bebida_num==1:
        bebida+=2
    if bebida_num==2:
        bebida+=1.5
    if bebida_num==3:
        bebida+=1
    resultado=menu+acompañamiento+bebida
    acumulado+=resultado
    veces+=1
    repeticion=input("¿Quieres otro pedido? (s/n)")
    if repeticion==n:
        chivato+=1
    else:
acumulado_iva= acumulado + (acumulado*0.10)
print("""RESUMEN
Número de pedidos: {veces}
Total a pagar: {acumulado}
Total con iva: {acumulado_iva}""")
if acumulado>10 and acumulado<20:
    acumulado_final=acumulado_iva-acumulado_iva*5
    print("Precio total con descuento del 5%: {acumulado_final}")
if acumulado>30:
    acumulado_final=acumulado_iva-acumulado_iva*15
    print("Precio total con descuento del 15%: {acumulado_final}")

