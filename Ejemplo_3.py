'''
En el tercer ejemplo vamos a crear una función que
cuenta cuántos de los números que hay dentro de una lista
son divisibles por 10.

La función tomará como argumento una lista de números y
debe regresar la cuenta que representa la cantidad de números
en la lista que son divisibles por 10.

Para realizar este ejemplo debemos seguir estos pasos:

1. Definir una función que acepte un argumento.
2. Inicializar un contador en 0
3. Iterar a través de los elementos de la lista.
4. Dentro del ciclo validar si ese número es divisible por 10,
    de ser así, incrementar el contador
5. Al finalizar todas las iteraciones, regresar la cuenta.'''

def divisible_diez(numeros):
    cuenta = 0
    for numero in numeros:
        if numero % 10 == 0:
            cuenta += 1
    return cuenta

print(divisible_diez([10, 15, 20, 30, 45, 60]))
