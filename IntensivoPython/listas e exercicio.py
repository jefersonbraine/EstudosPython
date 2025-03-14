# Lista: representa uma sequência de valores / Array

# Sintaxe: nome_lista = [valores, ]

# n1 = [4,6,7,8,0,2]
# n2 = [1,4,7,8,12,5]
# valores = n1 + n2
# valores[0] = 9
# print(valores[0])

#Sequenciais

# n1 = [4,6,7,8,0,2]
# n2 = [1,4,7,8,12,5]
# valores = n1 + n2
# valores[0] = 9
# print(valores[0:2])

# print(len(valores)) #quantidade de elementos = length
# print(sorted(valores)) #versão ordenada da lista
# print(sorted(valores, reverse=true)) #ordem inversa
# print(sum(valores)) #soma todos os valores na lista
# print(min(valores)) #valor minimo
# print(max(valores)) #valor maximo

#! MANIPULAR DADOS DA LISTA

#APPEND - acrescenta um valor no final da lista

# valores.append(13)

# #pop - tira o ultimo item da lista

# valores.pop()

#inserir em uma posição especifica

#insert
# valores.insert(2, 90) #primeira a posição e depois o valor


#in verificar se tem um valor dentro de uma lista

# print (12 in valores) #true or false


# #! LAÇO FOR
# planetas = ['terra', 'marte', 'lua', 'júpiter', 'venus', 'mercúrio']
# for planeta in planetas:
#     print(planeta)


#!              EXERCICIO - MINHA RESOLUÇÃO

bebida = input('Digite suas cinco bebidas favoritas: ')

lista = bebida.split(',')
lista.sort()

for bebida in lista:
    print(bebida.strip())


#!              Resolução da aula

bebidas = []

for i in range(5):
    print(f'Digite uma bebida favorita: ')
    bebida = input()
    bebidas.append(bebida)

bebidas.sort()

print(f'\nBebidas escolhidas: ') #opcional
for bebida in bebidas: 
    print(bebida)

print(f'\nSaúde!') #opcional

