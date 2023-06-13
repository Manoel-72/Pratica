"""Exercicio intermediario de inicainte Primeiro Media de numero """

# Solicita ao usuario a quantidade de números
_quant_ = int(input("Digite a quantidade de números: "))

# Cria uma lista vazia para armazenar os números
numeros = []

# Solicita ao usuário os números e adiciona-os a lista
for i in range(_quant_):
    numero = float(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

# Calcula a media
media = sum(numeros) / len(numeros)

# Exibe o resultado utilizando f-string
print(f"A media dos números é: {media}")
