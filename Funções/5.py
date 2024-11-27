def numeros_pares(lista):
    """Retorna uma nova lista contendo apenas os números pares da lista original."""
    return [num for num in lista if num % 2 == 0]

# Testando a função
print(numeros_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Exemplo de uso