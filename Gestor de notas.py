nombre= input ('¿Como te llamas?')
print(f'Hola, {nombre}')
nota_mates= float(input('¿Cual ha sido tu nota de matematicas?'))
nota_historia= float(input('¿Cual ha sido tu nota de Historia?'))
nota_ingles= float(input('¿Cual ha sido tu nota de Inglés?'))
if nota_mates < 0 or nota_mates>10 or nota_historia<0 or nota_historia>10 or nota_ingles<0 or nota_ingles > 10:
    print('Tu nota puede ir de 0 a 10')
else:
    media=(nota_mates+nota_historia+nota_ingles)/3
    print(f'Tu media es de un {media:.2f}')
    if media >=5:
        print('Enhorabuena, has aprobado')
    else:
        print('Lo siento, has suspendido')
    nota_maxima= max(nota_mates,nota_historia,nota_ingles)
    nota_minima= min(nota_mates,nota_historia,nota_ingles)
    print('Resumen de resultados:')
    print(f'Nombre del alumno: {nombre}')
    print(f'Nota media de: {media}')
    print(f'Tu nota más alta ha sido de un {nota_maxima}')
    print(f'Tu nota más baja ha sido de un {nota_minima}')



