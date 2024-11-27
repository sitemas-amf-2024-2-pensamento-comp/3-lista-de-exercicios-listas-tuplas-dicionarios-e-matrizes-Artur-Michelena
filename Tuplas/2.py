# Criando a tupla pontos
pontos = (100, 200, 300)

# Tentando alterar o primeiro elemento da tupla
try:
    pontos[0] = 150
except TypeError as e:
    print("Erro ao tentar modificar a tupla:", e)