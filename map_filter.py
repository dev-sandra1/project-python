numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar los números pares
numeros_pares = filter(lambda x: x % 2 == 0, numeros)

# Elevar al cuadrado los números filtrados
resultado = list(map(lambda x: x**2, numeros_pares))

print(resultado) 