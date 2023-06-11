# Valor de pi com variavel
pi = 3.14159

# Raio da area, em float um procua um entra para mensagem Digite o raio de circulo
raio = float(input("Digite o raio do circulo"))

# Area e igual a pi vez o raio  com exponeciação de 2
area = pi * raio**2

# Aqui imprime o resultado  {} e area que sera formatada com numero de ponto fluante 2f
print(f"A area do circulo é {area:.2f}")
