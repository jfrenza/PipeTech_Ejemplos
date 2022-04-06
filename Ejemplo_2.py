'''
Para este ejemplo crearemos una función que combine
dos listas y al mismo tiempo organice los valores de menor a mayor.

Para realizar esto debemo seguir estos pasos:

1. Crear una función que acepte 2 argumentos, cada una de las listas
2. Combinar ambas listas
3. Ordenar los valores
4. Regresar el resultado.'''

def combinar_listas(lista1, lista2):
    lista_nueva = sorted(lista1 + lista2)
    return lista_nueva

print(combinar_listas([1, 2, 3], [-1, -2, 0]))
