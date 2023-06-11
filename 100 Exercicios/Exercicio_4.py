# Solicita  o nome e idade da pessoa das tres pessoas
nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = input("Digite o idade da primeira pessoa: ")

nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = input("Digite o idade da segunda pessoa: ")

nome3 = input("Digite o nome da terceira pessoa: ")
idade3 = input("Digite o idade da terceira pessoa: ")

# Vefirica quem é a pessoa mais velha
if idade1 >= idade2 and idade1 >= idade3:
    pessoa_mais_velha = nome1
 # Checa as idades
elif idade2 >= idade1 and idade2 >= idade3:
    pessoa_mais_velha = nome2
# informa condição de mas sobre as idades
else:
    pessoa_mais_velha = nome3

# Imprime o resultado da pessoa mais velha entre as tres
print(f"A pessoa mais velha é: {pessoa_mais_velha}")
