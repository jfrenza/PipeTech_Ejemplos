'''
Para el último ejemplo vamos a crear una función que acepte un
diccionario como argumento.

Este diccionario tendrá como llaves diferentes apellidos y en valores
una lista de nombres de personajes que tengan ese apellido.

La función debe calcular el número de personas que tienen la misma
primera letra en el apellido

Para lograr este objetivo debemos:

1. Definir una función que tome como argumento el diccionario
2. Crear un nuevo diccionario vacío.
3. Iterar a través de cada una de las llaves.
4. Dentro del ciclo validar si la primera letra del apellido no está en el diccionario,
    de ser así, añadirla con 0 en su valor; de lo contrario incrementar el valor de la cuenta.
5. Al final del ciclo regresar el nuevo diccionario'''


nombres = {"Kamado": ["Tanjiro", "Nezuko", "Tanjuro"], "Rengoku" : ["Kyojuro", "Senjuro"], "Tomioka": ["Giyu"]}

def cuenta_primer_apellido(nombres):
    letras = {}
    for key in nombres:
        primera_letra = key[0]
        if primera_letra not in letras:
            letras[primera_letra] = 0
        letras[primera_letra] += len(nombres[key])
    return letras

print(cuenta_primer_apellido(nombres))
