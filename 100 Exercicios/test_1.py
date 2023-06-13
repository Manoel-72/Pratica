"""Exercicio avançado de python sobre conta bancaria depositar,sacar e verifica"""


class ContaBancaria:
    # Onde você pode definir atributos iniciais ou realizar outras operações de inicialização no método __init__.
    def __init__(self):
        self.saldo = 0  # Inicializa o saldo da conta como zero

    # É uma declaração de uma função chamada depositar. Nesse caso, a função é definida dentro de uma classe, tornando-se um método da classe ContaBancaria.
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor  # Adiciona o valor depositado ao saldo da conta
            print(f"Deposito de {valor} realizado com sucesso.")
        else:
            print("Valor inválido para deposito")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor  # Subtrai valor sacado do saldo da conta
            print(f"Saque de {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou Valor inválido para saque.")

    def obter_saldo(self):
        return self.saldo  # Retorna o saldo atual da conta


conta = ContaBancaria()
print(f"Saldo inicial: {conta.obter_saldo}")

valor_deposito = float(input("Digite um valor para deposito: "))
conta.depositar(valor_deposito)

valor_saque = float(input("Digite um valor para sacar: "))
conta.sacar(valor_saque)

saldo_atual = conta.obter_saldo()  # Obtem o Saldo atual da conta
print(f"Saldo atual: {saldo_atual}")
