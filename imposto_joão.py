# Valor da renda anual de João
renda_anual = float(input("Digite o valor da renda anual de João: "))

# Verifica se João paga imposto
if renda_anual <= 30000:
    print("João está inseto de pagar imposto.")

else:
    imposto = renda_anual * 0.15

    print("João deve paga R$ {:.2f} de imposto.".format(imposto))
