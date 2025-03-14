
#*Sintaxe:
#*print(objetos, argumentos)

# mensagem = 'Função print()'
# print(mensagem) #!imprimindo uma variável

# print('Aula de python') #!imprimir string direto

# nome = 'Seu nome aqui'
# canal = 'treinamentos'
# print('Treinamentos -', nome) #!argumento posicional
#print(canal, '-', nome)


#!concatenar strings
# nome = input('Digite seu nome: ')
# msg = 'Olá ' + nome + '! Bem vindo!'
# print('Olá ' + nome + '! Bem vindo!')
# print(msg)

#! Desabilitar quebra de linha

# print('imprime a mensagem e muda de linha')
# print('imprime a mensagem e permanece na linha.', end='')
# print(' Continuo na mesma linha!')

#! String complexas
# nome = 'Maria'
# idade = 30
# msg_formatada = 'O nome dela é {0} e ela tem {1} anos'.format(nome, idade)
# print(msg_formatada)

#! F string - meais fácil e eficiente
# nome = 'Fabio'
# peso = 105.02
# msg = f'Olá, meu nome é {nome} e eu peso {peso} quilos'
# print(msg)

# print(f'Olá, meu nome é {nome} e eu peso {peso} quilos') #! Tem como fazer desse jeito também

# a = 10
# b = 5
# res = f'A soma de {a} com {b} é igual a {a+b}'
# print(res)

valor = 172.65789206
# # print(f'O valor é {valor}')
# print(f'O valor é {valor:.2f}') #!formatando o valor

# print(f'O valor é \'{valor:.2f}\'') #!se precisar usar aspas, caractere de escape

nome = 'Joao'
idade = 32
print(f'Nome:\t{nome}\tIdade:\t{idade}') #tabulação

