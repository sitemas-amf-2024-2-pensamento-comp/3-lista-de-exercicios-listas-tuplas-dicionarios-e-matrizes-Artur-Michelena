def fibonacci(n):
    """Retorna uma lista com os n primeiros números da sequência de Fibonacci."""
    if n <= 0:
        return []
    sequencia = [0, 1]
    while len(sequencia) < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia[:n]

# Testando a função
print(fibonacci(10))  # Exemplo de uso