nombre= input('Escriba su nombre: ')
numero_de_productos= int(input('Cuántos productos quiere comprar: '))
def calcular_importe(precio, unidades):
    resultado = precio * unidades
    return resultado
subtotal= 0
nombres_productos=[]
precios_productos=[]
unidades_productos=[]
for producto in range(numero_de_productos):
    nombre_producto= input(f'Escriba el nombre del producto {producto+1}: ')
    nombres_productos.append(nombre_producto)
    precio_producto= float(input('Escriba el precio del producto: '))
    precios_productos.append(precio_producto)
    unidades_producto=int(input('Escriba las unidades que quiere comprar del producto: '))
    unidades_productos.append(unidades_producto)
    importe_total= calcular_importe(precio_producto, unidades_producto)
    print(f'El importe total es: {importe_total:.2f}€')
    subtotal+= importe_total
print('-------FACTURA------')
for num in range(len(nombres_productos)):
    importe=calcular_importe(precios_productos[num], unidades_productos[num])
    print(f'El precio de {nombres_productos[num]} es de {precios_productos[num]} y ha decidido comprar {unidades_productos[num]} unidades, por lo que el precio total de {nombres_productos[num]} es de {importe:.2f}€')
print(f'Subtotal: {subtotal:.2f}')

