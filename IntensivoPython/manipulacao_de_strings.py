# nome = 'Curso de '
# tema = 'Python'
# print(nome + tema)
# print(len(nome))#tamanho da string

frase = 'Vamos aprender Python hoje.'
palavras = frase.split()#lista de strings ['Vamos', 'aprender', 'Python', 'hoje.']
print(palavras)
print(palavras[1])

for palavra in palavras: # separa palavra por palavra  uma linha separada
    print(palavra)

for letra in frase: # separa letra por letra em uma linha separada com seu número de indice
    print(letra)

#slicing em strings

print(frase[0:5])
print(frase[7:19])
print(frase[-3:])

#find encontrar
# email = input('Digite seu endereço de email: ')
# arroba = email.find('@')#vai encontrar em que posição esse caractere vai estar
# print(arroba) 

# #slice separar o nome do usuario do dominio
# usuario = email[0:arroba]
# dominio = email[arroba+1:]
# print(usuario)
# print(dominio)

#operadores de assocoação in e not in
produtos = 'Carbonato de sódio e óxido de zinco'
print ('sódio' in produtos)
print ('magnésio' in produtos)
print ('magnésio' not in produtos)

#find pode ser usado para encontrar a primeira ocorrencia ou inicio de substring
item = 'hipoclorito'
pos = item.find('clor') # 4
print(pos)
pos = item.find('flu') # -1
print(pos)

#trabalhar com maisculos e minusculos

objeto_celeste = 'galaxia esPiral M31'
print(objeto_celeste.upper())# todo em maiúsculo uppercase
print(objeto_celeste.lower())# todo em minúsculo lowercase
print(objeto_celeste.capitalize())# primeira letra em maiuscula
print(objeto_celeste.title())# a primeira letra de casa palavra em maiuscula

# Substituir um elemento de string
suplemento = 'cloreto de magnésio'
n_suplemento = suplemento.replace('magnésio', 'Zinco')
print(suplemento)
print(n_suplemento)


#espaços em branco
frase = '      marea turbo pegando fogo       '
print(frase)

print(frase.lstrip())
print(frase.rstrip())
print(frase.strip())


#alinhamento de texto

fruta = 'abacate'
print(fruta)
print(fruta.rjust(20))#right justify (justificar a direita)
print(fruta.center(20))#centralizar
print(fruta.ljust(20, '-'))#left justify (justificar a esquerda)
print(fruta.center(20, '-'))#centraliza e preenche os espaços com o que eu quiser


#prefixos e sufixos

p = 'Bóson de riggs'
print(p.startswith('on'))#começa com (é uma pergunta)
print(p.endswith('s'))#termina com (é uma pergunta)


# docstrings (strings literais como comentários, usado para documentar certos trechos do código)

texto = '''
Docstring é uma espécie de documentaçào que podemos inserir dentro de um módulo, função ou classe no Python entre outros locais.
    Respeita identações e é multilinhas
'''

print(texto)