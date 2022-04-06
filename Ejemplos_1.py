'''
Para el primer ejemplo, debemos crear una función que valide si
el resultado de número a elevado a otro número b es mayor que cierto número c

Para alcanzar ese objetivo debemos seguir los siguientes pasos:

1. Definir una función que acepte 3 argumentos: base, exponente, resultado_esperado.
2. Calcular el resultado de la base elevado al exponente.
3. Usando un condicional validar si el resultado es mayor o menor que el argumento.
4. Regresar un String que contenga la respuesta buscada '''

def potencia_mayor(base, exponente, resultado_esperado):
    respuesta = base ** exponente
    if respuesta > resultado_esperado:
        return f''' El resultado esperado es menor a la respuesta.
                    La solución es: {respuesta}'''
    else:
        return f'''El resultado esperado es mayor a la respuesta.
                La solución es: {respuesta}'''


print(potencia_mayor(10, 2, 90))
