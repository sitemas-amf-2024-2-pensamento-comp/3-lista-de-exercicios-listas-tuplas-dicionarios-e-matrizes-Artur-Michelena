# Lista para armazenar a sequência de números
numeros = []

# Solicitando ao usuário os números
print("Digite 10 números:")
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

# Criando as listas de pares e ímpares
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

# Exibindo as listas
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")