'''
Para el ejemplo cuatro vamos a crear una función que calcule
el porcentaje de victorias de un equipo de futbol.

Para hacer ese cálculo vamos a necesitar dos argumentos,
la cantidad de victorias y la cantidad de derrotas.

Para alcanzar el objetivo debemos seguir los pasos:

1. Definir una función que tome dos argumentos, Victorias y Derrotas
2. Calcular el número total de partidos jugados
3. Calcular el ratio de Victorias.
4. Convertir el ratio en porcentaje
5. Regresar el porcentaje.'''

def porcentaje_victorias(victorias, derrotas):
    total = victorias + derrotas
    ratio = victorias / total
    return round(ratio * 100, 2)

print(porcentaje_victorias(20, 5))
