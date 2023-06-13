"""Exercicio de calculo total dos segundos do livro"""


def calcular_segundos():
    dias = int(input("Digite a Quantidade de dias: "))
    horas = int(input("Digite a Quantidade de horas: "))
    minutos = int(input("Digite a Quantidade de minutos: "))
    Segundos = int(input("Digite a Quantidade de segundos: "))

    total_segundos = Segundos + (minutos * 60) + \
        (horas * 3600) + (dias * 86400)

    print(f"O total em segundos é : {total_segundos} segundos")


calcular_segundos()
