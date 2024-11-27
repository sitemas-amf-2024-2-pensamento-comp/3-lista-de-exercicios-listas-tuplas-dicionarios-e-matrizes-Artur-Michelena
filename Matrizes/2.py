# Dada a matriz
numeros = [[2, 4], [6, 8]]

# Calculando a soma de todos os elementos
soma = sum(sum(linha) for linha in numeros)

# Imprimindo a soma
print(f"A soma de todos os elementos é: {soma}")