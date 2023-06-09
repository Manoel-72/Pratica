familia = ["Manoel", "Mae", "Giovanna", "Joao"]
#              0     1     2       3
#              -4    -3    -2      -1
# print(familia[3])
# print(familia[-3])
# print(familia[2:3])

print(familia)
familia[3] = "Manoel"  # alterar o valor
print(familia)

# Adicionamos outra lista criando um variavel com essa lista
familia.extend(["Olivia e Oliver"])
print(familia)

familia.append("filhos")  # adiciona so um valor
print(familia)
familia.insert(1, "Filhos")  # inserir Filho na segunda camada
familia.pop()  # sempre remove o Ultimo
familia.pop()  # sempre remove o Ultimo
familia.remove("Mae")  # remove nome
familia.clear()
print(familia)
print(familia.count("Manoel"))
