# Dicionários em pares chave, valor (hashmaps e arrays de outras linguagens, objeto de JavaScript)

elemento = { #não pode ter chaves repetidas
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(f'Elemento: {elemento['nome']}')
print(f'Densidade: {elemento['densidade']}')

print(f'O dicionário possui {len(elemento)} elemntos.')

# Atualizar uma entrada (valor associado a uma chave e não a chave em si)

elemento['grupo'] = 'Alcalinos'
print(elemento)

# Adicionar uma entrada (cria a chave e insere no dicionário)
elemento['período'] = 1
print(elemento)

# # Exclusão de itens em dicionários
# del elemento['período']
# print(elemento)


# # apagar todos os itens de dentro do dicionário
# elemento.clear()
# print(elemento)

# #apaga tudo até o dicionário
# del elemento
# print(elemento)

#retornar items do dicionário

print(elemento.items()) # dict_items([('Z', 3), ('nome', 'Lítio'), ('grupo', 'Alcalinos'), ('densidade', 0.534), ('período', 1)])

for i in elemento.items():
    print(i)


# método keys
print(elemento.keys()) 

for i in elemento.keys():
    print(i)


# método values
print(elemento.values()) 

for i in elemento.values():
    print(i)


#desempacotar as chaves e valores simultaneamente

for i, j in elemento.items():
    print(f'{i}: {j}')
