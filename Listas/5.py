# Lista para armazenar as idades
idades = []

# Loop para solicitar as idades ao usuário
while True:
    idade = int(input("Digite uma idade (ou 0 para finalizar): "))
    if idade == 0:
        break
    idades.append(idade)

# Calculando a média das idades
if idades:  # Verifica se a lista não está vazia
    media = sum(idades) / len(idades)
    print(f"A média das idades é: {media:.2f}")
else:
    print("Nenhuma idade foi digitada.")