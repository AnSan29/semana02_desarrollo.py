# ----------------->>> DEFINICION DE FUNCIONES <<<-----------------

# 1- Función para solicitar numero entero.
def cant_calificaciones_funcion():
    while True:
        try:
            print(' ')
            print('Ingrese cantidad de calificaciones a ingresar:')
            cantidad_calificaciones = int(input(' => '))
            if cantidad_calificaciones < 0:
                print(' ')
                print('Error! -> No se permiten numeros negativos.')
                print(' ')
            else:
                return cantidad_calificaciones
        except ValueError:
            print(' ')
            print('Error! -> valor inválido: "No se permite nada diferente a numeros positivos".')
            print(' ')
    
# 2- Función para solicitar calificaciones.
def calificaciones_add_funcion():
    for i in range(cantidad_calificaciones):
        while True:
            try:
                print(' ')
                print(f'Ingrese la {i+1} calificación de {cantidad_calificaciones}:')
                calificacion = float(input('=> '))
            
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

# 3- Función para solicitar calificacion a comparar.
def valor_comparar_funcion():
    while True:
        try:
            print(' ')
            print('Ingresar valor a buscar en lista:')
            valor_comparar = float(input('=> '))
            
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


# Declaración de variables generales.
lista_calificaciones = []
suma_notas = 0
minimo_aprobar = 60.0
estado_aprobacion = ''

# ------------------------->>> ENTRADAS <<<-------------------------
# Obtenemos cantidad de notas a ingresar.
cantidad_calificaciones = cant_calificaciones_funcion()
print(f'se registrarán: ({cantidad_calificaciones}) calificaciones.')

# Obtenemos calificaciones.
calificacion = calificaciones_add_funcion()     

# Obtenemos el valor a comparar.
valor_comparar = valor_comparar_funcion()

# ------------------------->>> PROCESO <<<-------------------------
# Hallamos el promedio.
for nota in lista_calificaciones:
    suma_notas += nota
    promedio_estudiante = suma_notas/cantidad_calificaciones

# Hallamos estado de aprobación.
if promedio_estudiante > minimo_aprobar:
    estado_aprobacion = 'Aprobado'
else:
    estado_aprobacion = 'Reprobado'

# Hallamos cantidad de calificaciones mayores.
es_mayor = 0
i = 0
while i < cantidad_calificaciones:
    nota = lista_calificaciones[i]
    if nota > valor_comparar:
        es_mayor+=1
    i+=1

# Hallamos cuantas veces aparece el valor en nuestra lista.
aparicion = 0
for nota2 in lista_calificaciones:
    if nota2 == valor_comparar:
        aparicion +=1
        continue


# ------------------------->>> SALIDAS <<<-------------------------
print(' ')
print('-'*20)
print(f'Lista de calificaciones: {lista_calificaciones}')
print('--------------------')
print(f'suma de calificaciones:          {suma_notas:.2f}')
print(f'promedio estudiante:             {promedio_estudiante:.2f}')
print(f'estado de aprobación:            {estado_aprobacion}')
print('--------------------')
print(f'se encontraron {es_mayor} notas mayores a: {valor_comparar}')
print(f"La calificación {valor_comparar} aparece {aparicion} veces.")
print('--------------------')
print(' ')
