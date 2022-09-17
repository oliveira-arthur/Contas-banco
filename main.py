from contas import CartaoCredito, ContaCorrente

#programa

conta_Arthur = ContaCorrente("Arthur","123.123.123-45", 123, 246755)
conta_Arthur.consultar_saldo()

#depositar dinheiro na conta
conta_Arthur.depositar(10000)
conta_Arthur.consultar_saldo()


#sacar dinheiro da conta
conta_Arthur.sacar_dinheiro(2000)
conta_Arthur.consultar_saldo()
conta_Arthur.sacar_dinheiro(40000)


print('=-'*20)
conta_Joaquim = ContaCorrente('joaquim','222.333.444-78','2345','234678')
conta_Arthur.transferir( 1000, conta_Joaquim)
conta_Arthur.transferir( 9000, conta_Joaquim)

conta_Arthur.consultar_saldo()
conta_Joaquim.consultar_saldo()

print('='* 20)
conta_Arthur.historico_transacoes()
conta_Joaquim.historico_transacoes()


print('=-'* 40)
cartao_arthur = CartaoCredito('Arthur', conta_Arthur)
print(cartao_arthur.conta_corrente._num_conta)
print(cartao_arthur.titular)



print(cartao_arthur.validade)
print(cartao_arthur.numero)
print(cartao_arthur.cod_segurança)

cartao_arthur.senha = '2345'
print(cartao_arthur.senha)

print(conta_Arthur.__dict__)