# Criando a matriz 3x3 com espaços vazios
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

# Marcando um "X" na posição central
tabuleiro[1][1] = "X"

# Imprimindo a matriz
for linha in tabuleiro:
    print(" | ".join(linha))