# Definindo função para cacular nota media
def calcular_nota(notas):
    return sum(notas) / len(notas)

# Definindo uma função para verificar se o aluno foi aprovado ou reprovado


def verificar_aprovado(media):
    if media >= 18.2:
        return "Aprovado"
    else:
        return "Reprovado"


# Coletar dados sobre aprovação do aluno
nota1 = float(input("Digita a nota do primeiro Semestre: "))
nota2 = float(input("Digita a nota do Segundo Semestre: "))
nota3 = float(input("Digita a nota do Terceiro Semestre: "))
nota4 = float(input("Digita a nota do Quarto Semestre: "))

# Colocar as notas em uma lista
notas = [nota1, nota2, nota3, nota4]

# Calcular a media
media = calcular_nota(notas)

# Verificando status se a nota do aluno foi aprovado ou reprovado
status = verificar_aprovado(media)

print(f"A media do aluno e {media:.2f} e ele foi {status}")
