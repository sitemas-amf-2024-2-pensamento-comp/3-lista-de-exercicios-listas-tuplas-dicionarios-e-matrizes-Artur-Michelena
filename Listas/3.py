# Criando a lista
temperaturas = [30, 22, 25, 28, 31, 27, 29]

# Aumentando em 5 graus as temperaturas menores que 25
temperaturas = [temp + 5 if temp < 25 else temp for temp in temperaturas]