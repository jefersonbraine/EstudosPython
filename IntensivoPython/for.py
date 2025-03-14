

# lista = [2,5,6,4,1,2,5,6,7,8,9,15,17,19,20]
# palavra = 'Bóson'

# for letra in palavra:
#     print(letra)

# for numero in range(1, 11): # de 1 a 10, parando no 1, se colocar só o número 10 apenas vai aparecer do 0 a 9
#     print(numero) #geração de faixa de valores

# nome = input('Digite seu nome: ')
# for x in range(10):
#     print(f'{x+1} {nome}') # 10 nome digitado

#* a função range pode operar com até 3 elementos
#* range(valor_inicial, valor_final, incremento)

# for x in range(2, 20, 2): #ou (20, 1, -2)
#     print(x)


pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina')
# tirar o quartzo

for pedra in pedras: #sequencia tulpula
    if pedra == 'Quartzo':
        continue #encerra a iteração atual do laço
    print(pedra)

