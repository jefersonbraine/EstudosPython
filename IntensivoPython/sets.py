# Sets são conjuntos, coleções não ordenadas de valores únicos, que se usa para armazenar múltiplos items dentro de um objeto (armazena apenas itens não duplicados e suporta operações matemáticas sobre conjuntos)

planeta_anao = {'Plutao', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(planeta_anao) # {'Eris', 'Ceres', 'Plutao', 'Haumea', 'Makemake'}

print(len(planeta_anao)) # quantidade de items
print('Lua' not in planeta_anao)
print('Lua' in planeta_anao)

for astro in planeta_anao:
    print(astro.upper(), end=' ') #UM EM CADA LINHA COM END=" " sem ele fica em forma de lista

for astro in planeta_anao:
    print(astro.upper()) # fica em forma de lista

astros = ['Lua', 'Venus', 'Sirius', 'Marte', 'Lua']
print(astros, end=' ')
astro_set = set(astros)
print(astro_set) # não vai aparecer a lua duas vezes

astros1 = {'Lua', 'Venus', 'Sirius', 'Marte'}
astros2 = {'Lua', 'Venus', 'Sirius', 'Marte', 'Cometa de Halley'}# print(astros1 == astros2) #$ão iguais?
# print(astros1 != astros2) # São diferentes? ! =

print(astros1 | astros2) #união de conjuntos
print(astros1.union(astros2)) #união de conjuntos exemplo 2

print(astros1 & astros2) #intersecção
print(astros1.intersection(astros2)) #intersecção exemplo 2

print(astros1 ^ astros2) #diferença simétrica de conjuntos
print(astros1.symmetric_difference(astros2)) #união de conjuntos exemplo 2


#adicionar elementos

astros1.add('Uranos')
astros1.add('Sol')

print(astros1) #aparecem em uma ordem aleatória

#remover elementos
astros1.remove('Sol')
astros1.remove('Plutao') #! KeyError: 'Plutao
astros1.discard('Plutao') # Não dá erro mesmo Não tendo o que eu pedi pra tirar
print(astros1)

# Remover elemento arbitrário
astros1.pop() #ele remove um dos elementos (de forma aleatória)

#Se precisar limpar todo o conjunto
astros1.clear() #limpa tudo e só aparece set()