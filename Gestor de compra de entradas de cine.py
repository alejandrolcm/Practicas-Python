nombre_usuario= input('Escriba su nombre de usuario: ')
numero_peliculas= int(input('¿Cuantas peliculas desea comprar?: '))
def calcular_precio (precio, cantidad):
    importe_total = cantidad*precio
    return importe_total
nombres_peliculas= []
precios_entradas=[]
numero_entradas=[]
totales1=[]
total=0
for lista_pelicula in range(numero_peliculas):
    nombre_peli= input(f'Escriba el nombre de la pelicula {lista_pelicula+1}: ')
    nombres_peliculas.append(nombre_peli)
    precio_entr= float(input(f'Escriba el precio de la pelicula {lista_pelicula+1}: '))
    precios_entradas.append(precio_entr)
    numero_entr= int(input('Escriba el numero de entradas que desea: '))
    numero_entradas.append(numero_entr)
    totales= calcular_precio(precio_entr, numero_entr)
    totales1.append(totales)
    total+=totales
print('-------FACTURA------')
for pelis in range(len(nombres_peliculas)):
    print(f'{nombres_peliculas[pelis]}--- {precios_entradas[pelis]} x {numero_entradas[pelis]} entradas = {totales1[pelis]}€')
print('-----TOTAL----')
print(f'{total:.2f}€')

