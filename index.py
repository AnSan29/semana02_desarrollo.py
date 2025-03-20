


lista_calificaciones_estudiante = []
calif_ingresadas = 0
minimo_aprobar = 60.0
# Damos instrucción de que 
print('Ingrese una calificación, escriba --> salir <-- para finalizar')
while True:
    print(' ')
    calificacion = input('Calificación => ')
    if (calificacion.replace(".", "", 1).isdigit() and float(calificacion) >= 0 and float(calificacion) <= 100):#---------| verifico que variable --> calificacion <-- sea un número válido.
        calif_ingresadas +=1 #-----------------------------------------------------------------------------------| incrementamos en uno por cada iteración.
        calificacionFloat = float(calificacion)#--------------------------------------------------------------------------| convierto el tipo de dato variable --> calificacionFloat <-- a tipo float.
        lista_calificaciones_estudiante.append(calificacionFloat)#--------------------------------------------------------| ingresamos el valor de calificacionFloat en la lista_calificaciones por cada iteración.
        longitud_lista = len(lista_calificaciones_estudiante)
        suma_list_calif_estudiante = sum(lista_calificaciones_estudiante)
        promedio_estudiante = suma_list_calif_estudiante / longitud_lista

        if promedio_estudiante < minimo_aprobar:
            estado_materia = 'aprobado'
        else:
            estado_materia = 'reprobado'
        
        
    else:
        print(' ')
        print('Error!!!')
        print('1. No puede ingresar letras.')
        print('2. No puede ingresar números negativos')
        print('3. la calificacion debe estar en el rango de (0-100)')
        print( f'calificaciones registradas: {lista_calificaciones_estudiante}')
        print(' ')

    if calificacion == 'salir':
        break

print( f'suma de notas: {suma_list_calif_estudiante}')
print(f'calificaciones registradas: {lista_calificaciones_estudiante}')
print(f'longitudLista: {longitud_lista}')
print(f'promedio: {promedio_estudiante}')