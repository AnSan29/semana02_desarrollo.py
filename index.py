#declaracion de variables
lista_calificaciones = []
suma_notas = 0

#declaracion de funciones 
# - solicitud numero entero inicial.
def cant_calificaciones_funcion():
    while True:
        try:
            print('Ingrese cantidad de calificaciones a ingresar:')
            cantidad_calificaciones = int(input(' => '))
            if cantidad_calificaciones < 0:
                print(' ')
                print('Error! -> No se permiten numeros negativos.')
                print(' ')
            else:
                break
        except ValueError:
            print(' ')
            print('Error! -> valor inválido: "No se permite nada diferente a numeros positivos".')
            print(' ')
    return cantidad_calificaciones
    
# - solicitar calificaciones
def calificaciones_add_funcion():
    for i in range(cantidad_calificaciones):
    
        while True:
            try:
                calificacion = float(input('Ingrese el valor de una calificación => '))
            
                if type(calificacion).__name__ == 'float':
                    if calificacion < 0 or calificacion >100:
                        print(' ')
                        print('Error! -> fuera de rango: "La calificación debe ser de 0 a 100".')
                        print(' ')
                    else:
                        break
            except ValueError:
                print(' ')
                print('Error! -> valor inválido: "No se permite nada diferente a numeros positivos".')
                print(' ')
    
        lista_calificaciones.append(calificacion) 

# - solicitar valor a comparar
def valor_comparar_funcion():
    while True:
        try:
            valor_comparar = float(input('Ingrese el valor a comparar => '))
            
            if type(valor_comparar).__name__ == 'float':
                if valor_comparar < 0:
                    print(' ')
                    print('Error! -> número negativo: "La calificación no puede ser negativa".')
                    print(' ')
                else:
                    return valor_comparar
        except ValueError:
            print(' ')
            print('Error! -> valor inválido: "No se permite nada diferente a numeros positivos".')
            print(' ')
    

#paso1
# pedimos cuantas notas ingresaremos

cantidad_calificaciones = cant_calificaciones_funcion()
print(f'se registrarán: ({cantidad_calificaciones}) calificaciones.')

#paso 2
calificacion = calificaciones_add_funcion()     

#hallando promedio
for nota in lista_calificaciones:
    suma_notas += nota
    promedio_estudiante = suma_notas/cantidad_calificaciones
minimo_aprobar = 60.0
estado_aprobacion = ''

if promedio_estudiante > minimo_aprobar:
    estado_aprobacion = 'Aprobado'
else:
    estado_aprobacion = 'Reprobado'

#paso 4
valor_comparar = valor_comparar_funcion()
print(valor_comparar)

# hallar cuantas calificaciones son mayores al valor ingresado
es_mayor = 0
i = 0
while i < cantidad_calificaciones:
    nota = lista_calificaciones[i]
    if nota > valor_comparar:
        es_mayor+=1
    i+=1

aparicion = 0
# verificacion y conteo
for nota2 in lista_calificaciones:
    if nota2 == valor_comparar:
        aparicion +=1
        continue


print('--------------------')
print(lista_calificaciones)
print(f'suma de calificaciones:({suma_notas})')
print(f'promedio estudiante: ({promedio_estudiante:.2f})')
print(f'estado de aprobación:({estado_aprobacion})')
print(f'se encontraron: {es_mayor} notas mayores a: ({valor_comparar})')
print(f"La calificación {valor_comparar} aparece {aparicion} veces.")
print('--------------------')
