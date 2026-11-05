
usuarios={}

def añadir_usuario():
    nombre = input('Nombre: ')
    if nombre in usuarios:
        print('El usuario ya existe')
        return
    else:
        try:
            edad = int(input('Edad: '))
        except ValueError:
            print('La edad debe ser un numero entero')
            return
        if edad>0:
            usuarios[nombre]=edad
            print('Usuario añadido correctamente')
        else:
            print('La edad debe ser mayor que 0')

def buscar_usuario():
    nombre_usuario = input('Nombre del usuario: ')
    if nombre_usuario in usuarios.keys():
        print(usuarios[nombre_usuario])
    else:
        print('El usuario no existe')

def mostrar_usuarios():
    if usuarios:
        print(usuarios)
    else:
        print('No hay usuarios')

while True:
    print('¿Que quieres hacer?')
    print("""1. Añadir usuario
    2. Buscar usuario
    3. Mostrar usuarios
    4. Salir""")

    seleccionar_opcion= int(input('Seleccionar opcion: '))
    if seleccionar_opcion==1:
        añadir_usuario()
    elif seleccionar_opcion==2:
        buscar_usuario()
    elif seleccionar_opcion==3:
        mostrar_usuarios()
    elif seleccionar_opcion==4:
        break
    else:
        print('Opcion invalida')