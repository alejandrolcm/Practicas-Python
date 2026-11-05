nombre_cliente= input('Nombre del cliente: ')
#Producto1
producto1= input('Producto 1: ')
while producto1.isdigit():
    print('El producto 1 es invalido')
    producto1= (input('Vuelva a introducir el producto 1: '))
precio_producto1= float(input('Precio: '))
while precio_producto1<1:
    print('El precio tiene que ser mayor que 0')
    precio_producto1= float(input('Introduce otro precio:'+ ' '))
unidades_producto1= int(input('Unidades: '))
while unidades_producto1<1:
    print('Las unidades deben de ser de 1 o mayor')
    unidades_producto1= int(input('Introduce otro numero de unidades: '))
#Producto2
producto2= input('Producto 2: ')
while producto2.isdigit():
    print('El producto 2 es invalido')
    producto2= input('Vuelve a introducir el producto 2: ')
precio_producto2= float(input('Precio: '))
while precio_producto2<1:
    print('El precio tiene que ser mayor que 0')
    precio_producto2= float(input('Introduce otro precio:'+ ' '))
unidades_producto2= int(input('Unidades: '))
while unidades_producto2<1:
    print('Las unidades deben de ser 1 o mayores')
    unidades_producto2= int(input('Introduce otro número de unidades: '))
print('======FACTURA======')
print(f'Cliente:{nombre_cliente}')
precio_total1= (precio_producto1*unidades_producto1)
precio_total2= (precio_producto2*unidades_producto2)
print(f'{producto1}: {precio_total1:.2f}€')
print(f'{producto2}: {precio_total2:.2f}€')
subtotal_pedido= (precio_total1+precio_total2)
print(f'Subtotal: {subtotal_pedido}€')
descuento=subtotal_pedido*0.10
total_con_descuento= subtotal_pedido-descuento
if subtotal_pedido>=100:
    print(f'Descuento: {descuento:.2f}€')
    print(f'Total: {total_con_descuento:.2f}€')
else:
    print(f'TOTAL: {subtotal_pedido:.2f}€')
print('===================')


