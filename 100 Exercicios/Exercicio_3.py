# Solicita que digite um número interio
numero = int(input("Digite um número interio: "))

# Verifica  se o numero é par ou ímpar
if numero % 2 == 0:
    resultado = "Par"
    
    # Mas Se numero for ímpa da isso
else:
    resultado = "Ímpar"
    
    print(f"O Número {numero} é {resultado}.")