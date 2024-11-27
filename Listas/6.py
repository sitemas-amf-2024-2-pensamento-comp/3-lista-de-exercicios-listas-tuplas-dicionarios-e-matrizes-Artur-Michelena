# Listas para armazenar as sequências
sequencia1 = []
sequencia2 = []

# Solicitando ao usuário os números da primeira sequência
print("Digite 5 números para a primeira sequência:")
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    sequencia1.append(numero)

# Solicitando ao usuário os números da segunda sequência
print("Digite 5 números para a segunda sequência:")
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    sequencia2.append(numero)

# Juntando as duas listas
lista_unida = sequencia1 + sequencia2

# Exibindo a lista unida
print(f"A lista unida é: {lista_unida}")