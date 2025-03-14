import random

# print('Gerar cinco números aleatórios entre 1 e 50: \n ')
# for i in range(5):
#     n = random.randint(1, 50)
#     print(f'Número gerado: {n}')

#gerar números flutuantes

# valor = random.random()
# print(f'Número gerado: {valor * 10} ') # *gera somente entre 0 e 1, para aumentar só multiplicar * pelo valor que quiser

# print(f'Número gerado: {round(valor * 10, 2)} ') #*se quiser arredondar quantas casas eu quiser

# !método uniform

# valor = random.uniform(1,100)
# print(f'Número: {round(valor, 4)}')

# !sortear um valor dentro de uma lista

# L = [2,4,6,8,9,3,234,342,2,65,2,1,321,543,564,76,867,6767,867,56,454,454,234,23,676,8,9,23,34,5,76767,67]
# n = random.choice(L)
# print(f'Número escolhido: {n}')


# !método sample
# L = [2,4,6,8,9,3,234,342,2,65,2,1,321,543,564,76,867,6767,867,56,454,454,234,23,676,8,9,23,34,5,76767,67]
# n = random.sample(L, 3)
# print(f'Número escolhido: {n}')

# !Embaralhar
L = [2,4,6,8,9,3,234,342,2,65,2,1,321,543,564,76,867,6767,867,56,454,454,234,23,676,8,9,23,34,5,76767,67]
print(f'Exibir a lista original; {L}')
print(f'Embaralhar a lista e exibi-la: ')
n = random.shuffle(L)
print(L)