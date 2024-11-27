# Definindo a função maior_numero
def maior_numero(lista):
    """Retorna o maior número de uma lista."""
    if not lista:
        return None  # Caso a lista esteja vazia
    return max(lista)

# Testando a função com diferentes listas
lista1 = [10, 20, 30, 40, 50]
lista2 = [5, -3, 7, 0, 2]
lista3 = []

print(f"O maior número da lista1 é: {maior_numero(lista1)}")
print(f"O maior número da lista2 é: {maior_numero(lista2)}")
print(f"O maior número da lista3 é: {maior_numero(lista3)}")  # Teste com lista vazia