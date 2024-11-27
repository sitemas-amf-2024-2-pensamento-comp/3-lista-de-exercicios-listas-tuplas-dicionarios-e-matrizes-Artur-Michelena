def media(lista):
    """Calcula e retorna a média de uma lista de números."""
    if not lista:  # Verifica se a lista está vazia
        return None
    return sum(lista) / len(lista)

# Testando a função
print(media([10, 20, 30, 40, 50]))  # Exemplo de uso