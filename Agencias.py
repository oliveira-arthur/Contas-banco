from random import randint

class Agencia:

    def __init__(self,telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []


    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'O valor do caixa esta abaixo do nivel recomendado para esta agência. Caixa atual: R${self.caixa:.2f} reais')
        else:
            print(f'O valor em caixa esta dentro do nivel recomendado. Caixa Atual:R$ {self.caixa:.2f} reais')


    def emprestar_dinheiro(self, valor, parcelas, cpf, salario_cliente, juros):
        valor_parcela = valor * juros / parcelas
        porcentagem_salario = salario_cliente * 0.3
        if valor_parcela < porcentagem_salario:
            print(f'O emprestimo foi concedido com sucesso! \n valor das parcelas: {valor_parcela}\n numero de parcelas{parcelas}')
        else:
            print(f'Emprestimo negado! O valor da parcela compromete mais de 30% do salario do cliente')


    def adicionar_cliente(self, nome, cpf , salario, dinheiro_aplicado):
        self.clientes.append((nome,cpf,salario, dinheiro_aplicado))




class AgenciaVirtual(Agencia):

    def __init__(self,site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0


    def depositar_paypal(self,valor):  #criar um if aqui dentro para que só transfira o dinheiro se tiver o valor em caixa
        if valor < self.caixa:
            self.caixa -= valor
            self.caixa_paypal += valor
        else:
            print('Valor indisponivel em caixa. Por favor, tentar outro valor.')


    def sacar_paypal(self, valor):
        if valor < self.caixa_paypal:
            self.caixa_paypal -= valor
            self.caixa += valor
        else:
            print('Valor indisponivel em caixa. Por favor, tentar outro valor.')





class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001,9999))
        self.caixa = 1000000




class AgenciaPremium(Agencia):


    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001,9999))
        self.caixa = 1000000


    def adicionar_cliente(self, nome, cpf , salario, dinheiro_aplicado):
        if dinheiro_aplicado >= 1000000:
            super().adicionar_cliente(nome, cpf, salario, dinheiro_aplicado)
        else:
            print('O Cliente não tem dinheiro aplicado o suficiente para se tornar cliente PREMIUM')

#if __name__ == '__main__': #isso aqui faz com que o codigo não rode quando for importado em outra aba.


print(1500 * 0.2)
agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br',36549898, 3333335667)
print(agencia_virtual.caixa)
print(agencia_virtual.clientes)
agencia_virtual.verificar_caixa()

agencia_comum = AgenciaComum(5666667,1000000678)
agencia_comum.verificar_caixa()
print(agencia_comum.numero)

agencia_virtual.depositar_paypal(20000)
print(agencia_virtual.caixa)
print(agencia_virtual.caixa_paypal)

agencia_premium = AgenciaPremium(344445666,2000999888)
agencia_premium.adicionar_cliente('Arthurzinho', 455555888,1500,10000)