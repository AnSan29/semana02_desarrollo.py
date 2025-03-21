# Funcionalidad del código.
La principal funcionalidad de este código es obtener una serie de calificaciones ingresadas por el usuario, para posteriormente ser almacenadas en una lista donde podremos llevar a cabo su análisis y también hallar valores estadísticos pertinentes a su calificación.

## Paso #1.
Declaración de funciones.
  1. `cant_calificaciones_function()`
```
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
```
Utilizamos un **ciclo while**, para poder validar que la cantidad ingresada sea un número entero positivo, implementamos condicionales para realizar las validaciones; si `cantidad_calificaciones` es un número negativo, mostrará un error ("no se permiten números negativos"). 
Si en `cantidad_calificaciones` se ingresan caracteres alfanuméricos, también mostrara un error ("no se permite nada diferente a números positivos").
Si ingresamos un numero valido, la función retornará el valor ingresado el input, dentro de la variable `cantidad_calificaciones`.

  2. `calificaciones_add_funcion()`
```
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
```
Implementamos un **ciclo for** donde se repetirá las veces indicadas en nuestra variable `cantidad_calificaciones`, ya que esta será la longitud de nuestro arreglo.
Con el **ciclo while** validamos que la `calificación` sea un valor correcto, y si no lo es, con los condicionales manejamos la entrega de errores. Si la `calificación` no esta en el rango (0-100); error (fuera de rango: “La calificación debe ser de 0 a 100”), si la `calificación` contiene caracteres alfanuméricos; error (valor inválido: “No se permite nada diferente a números positivos”)
si `calificación` es un numero valido, con el break rompemos el **cilo while** y añadimos por **cada iteracion del for** la `calificación` a la lista 
```
lista_calificaciones.append(calificacion) 
```
  3. `valor_comparar_funcion()`
```
def valor_comparar_funcion():
    while True:
        try:
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
```
Misma funcionalidad de `cant_calificaciones_function()`, pero en este caso la variable es llamada: `valor_comparar`

## Paso #2.
  1. Declaro las variables:
```
lista_calificaciones = []
suma_notas = 0
minimo_aprobar = 60.0
estado_aprobacion = ''
```

  2. Obtener valor de cantidad de calificaciones a ingresar por medio de la función: `cant_calificaciones_function()`
```
cantidad_calificaciones = cant_calificaciones_funcion()
print(f'se registrarán: ({cantidad_calificaciones}) calificaciones.')
```

  3. Obtener valor de calificaciones a añadir a lista por medio de la función: `calificaciones_add_funcion()`
```
calificacion = calificaciones_add_funcion()  
```

  4. Hallar el promedio del estudiante:
```
for nota in lista_calificaciones:
    suma_notas += nota
    promedio_estudiante = suma_notas/cantidad_calificaciones
```
utilizamos el **ciclo for** para iterar en la `lista_calificaciones` e incrementamos el valor de `suma_notas` sumando casa valor encontrado en la lista.
y en variable `promedio_estudiante` guardamos el resultado de la operacion para hallar este.

  5. Establecemos el valor de `estado aprobacion` según corresponda:
```
if promedio_estudiante > minimo_aprobar:
    estado_aprobacion = 'Aprobado'
else:
    estado_aprobacion = 'Reprobado'
```
Si el promedio del estudiante es mayor a la nota minima establecida según criterio, el estado de aprobacion es aprobado, de lo contrario, reprobado.

  6. Obtenemos el valor a comparar
```
valor_comparar = valor_comparar_funcion()
```
  7. Hallar cuantas calificaciones son mayores al valor ingresado
```
es_mayor = 0
i = 0
while i < cantidad_calificaciones:
    nota = lista_calificaciones[i]
    if nota > valor_comparar:
        es_mayor+=1
    i+=1
```
En la variable `es_mayor` contaremos la cantidad de numeros mayores a el valor guardado en `valor_comparar`.
Iniciamos el **ciclo wile** recorrieno la longitud de nuestro arrego, que en esta caso esta en la variable `cantidad_calificaciones`.
En cada iteracion guardamos en `nota` la calificacion obtenida y comparamos si la `nota` es mayor que el `valor_comparar`, si se cumple esta condicion, incrementamos el valor de `es_mayor`

  8. Hallar cuantas veces aparece el `valor_comparar` en mi lista de calificaciones.
```
aparicion = 0
for nota2 in lista_calificaciones:
    if nota2 == valor_comparar:
        aparicion +=1
        continue
```
En la variable `apricion` contaremos la cantidad de veces que aparezca.
con el **ciclo for** iteramos la variable `nota2` en la `lista_calificaciones` y comparamos si el valor de la variable `nota2` es igual a el valor de `valor_comparar`
si se cumple la condicion, entonces `apricion` incrementa su valor en 1 sino continuamos con la validación.

  9. Imprimir resultados:
```
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

```