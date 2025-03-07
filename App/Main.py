class Main:
    pass
#
# print("Testando o projeto")

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("João", "114444-2222")
conta=Conta(c1.get_nome(), 1222)

# conta=Conta(c1.get_nome, 6565, 0)


conta.deposita(100)
conta.saque(50)
conta.extrato()

# print(c1)
# print(c1.nome, " e ", c1.telefone)
# print(conta.titular, " Numero: ", conta.numero, " Seu Saldo: ", conta.saldo)