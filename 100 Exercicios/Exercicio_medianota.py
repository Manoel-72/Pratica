# obter notas do alunos
nota1 = float(input("Digite a nota do Primeiro semestre:"))
nota2 = float(input("Digite a nota do Segundo semestre:"))
nota3 = float(input("Digite a nota do Terceiro semestre:"))
nota4 = float(input("Digite a nota do Quarto semestre:"))

# Cacular a media do aluno
media = (nota1 + nota2 + nota3 + nota4) / 4

# Veficar se nota e suficiente para Aprovação do Aluno
if media >= 7.5:
    print("Parabéns foi aprovado! Boa ferias")
else:
    print("Infelizmente foi não foi Aprovado,Até Proxima")
