"""Exercicio de horario Conversor de horario"""


def hora(h, m):
    b = h / 12
    if b <= 1:
        hh = str(h)
        print("Sua hora: " + hh + ":", end='')
    elif b > 1 and b < 2:
        hhh = str(h - 12)
        print("Sua hora: " + hhh + ":", end="")
    else:
        print("formato de hora invalido")
        if b <= 1 and m <= 60:
            print(m, "a.m")
        elif b > 1 and m <= 60:
            print(m, "p.m")
        else:
            print("formato de minutos invalidos")
            while True:
                print("Digite 666 para sair")
                h = int(input("Informe a hora: "))
                if h == 666:
                    break
                m = int(input("Digite os minutos"))
                hora(h, m)


listpm = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
listam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]


def conversohorario():
    h = int(input("Digite a hora: "))
    m = int(input("Digite o minuto: "))
    if h in listam:
        idx = listam.index(h)
        print(f"São {h} : {m} A.M")
    elif h in listpm:
        idx = listpm.index(h)
        print(f"São {listpm[idx]} : {m} pm")
    else:
        print("Horario não reconhecido")


conversohorario()
