# São imutáveis (sequencia de constantes), mais rapidos que listas para iteração

# tuplas = (2,4,6,7,8,9)
# # tuplas[1] = 5 não funciona
# print(tuplas)

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'kr', 'Rn')

t1 = (5,6,7,9,12,2,3,4,7,9,0,5,6,9,9)
print(t1.count(5)) #ver quantas vezes aparece um elemento dentro da tupla (funciona pra strins repetidas também)

print(halogenios[0:2])#fazer slice

print('Cl' in halogenios)# Cl está presente dentro halogenios?

print(sum(t1))# somar todos
print(min(t1))# valor minimo
print(max(t1))# valor máximo

elementos = halogenios + gases_nobres #concatenar tuplas

print(elementos)

print(len(halogenios))#tamanho
print(halogenios[2])#posição
print(halogenios[-1])#posição de trás pra frente

#! Operações não disponiveis em tuplas: . sort(), .append(), .reverse(), .pop()... (todos os que alteram)

for elemento in elementos:
    print(f'Elemento químico: {elemento}')

#* Criar uma lista a partir de uma tupla
#função list

grupo17 = list(halogenios) #com isso podemos fazer alterações
grupo17[0] = 'H'
print(grupo17)


#* Criar uma tupla a partir de uma lista

grupo1 = ['li', 'na', 'k', 'Rb', 'cs', 'fr']
alcalinos = tuple(grupo1)
print(alcalinos)
print(type(alcalinos))

#organizar uma tupla, podemos criar uma nova tupla com os elementos de uma tupla classificados

print(sorted(alcalinos))