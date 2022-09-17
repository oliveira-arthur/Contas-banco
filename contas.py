from datetime import datetime
import pytz
from random import randint

class ContaCorrente:
    """
    Cria um obejto conta corrente para gerenciar as contas dos clientes.

    Atributos:
        nome (str): nome do titular da conta
        cpf (str): numero do cpf do cliente. Deve ser inserido com pontos e traços
        saldo: valor disponivel contido na conta do cliente
        agencia: Agencia responsavel pela conta do cliente
        limite: limite do qual o cliente dispõe para transações
        num_conta:  numero da conta do cliente
        transações: historico de transações feito pelo cliente

    """


    @staticmethod
    def _data_hora():
        fusoBR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fusoBR)
        return horario_BR.strftime('%d/%m/%y  %H:%M:%S')

    def __init__(self,nome,cpf,agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self._agencia = agencia
        self._limite = None
        self._num_conta = num_conta
        self._transacoes = []
        self.cartoes = []
        self.senha = []


    def consultar_saldo(self):

        print(f'Seu saldo atual é de R$ {self._saldo :,.2f}')

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Voce não tem saldo suficiente para essa operação')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def consultar_limite_cheque_especial(self):
        print(f'Seu limite do cheque especial é R${self._limite_conta() :,.2f}')

    def historico_transacoes(self):
        print('Historico de tranações:')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self,valor, conta_destino):
        if self._saldo - valor < self._limite_conta():
            print('Voce não tem saldo suficiente para essa operação')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
            conta_destino._saldo += valor
            conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fusoBR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fusoBR)
        return horario_BR

    def __init__(self,titular,conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}'
        self.cod_segurança = f'{randint(0,9)} {randint(0,9)} {randint(0,9)} '
        self.limite = 1000
        self._senha = '1234'         #restringindo a forma com  que o usuario muda o valor da senha
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self) #estou adicionando os cartões dentro da lista de cartçoes da  conta corrente

#depois criar o metodo get e o metodo set
    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
            print('Senha alterada com sucesso!')
        else:
            print('Não foi possivel alterar sua senha. SENHA INVALIDA!')



