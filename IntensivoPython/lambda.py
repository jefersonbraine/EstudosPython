
# *Funções lambda (anônimas) (sem nome, podem ser usadas e criadas no mesmo momento)
# *sintaxe:
#   *lambda argumentos: expressão

quadrado = lambda x: x**2

for i in range(1,11):
    print(quadrado(i))

#*é uma variável que se comporta como uma função
par = lambda x: x %2 == 0
print(par(8))

#*farenheit para celsius
f_c = lambda f: (f - 32) * 5/9
print(f_c(212))

#*Função map() #permite aplicar uma outra função a cada elemento de um objeto iteravel e retorna um objeto do tipo map. 

#*sintaxe
#*map(função, iteravel)

num = [1,2,3,4,5,6,7,8]
dobro = list(map(lambda x: x*2, num))

print(dobro)

palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
maiusculas = list(map(str.upper, palavras))
print(maiusculas)

#*Função filter() #filtra elementos de uma sequencia de acordo com um critério que a gente estabelece
# *Sintaxe:
# *filter (função, sequência)

def numeros_pares(n): 
    return n % 2 == 0

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

num_par = list(filter(numeros_pares, numeros))
print(num_par)

#*com lambda mas numeros impares

num_impar = list(filter(lambda x: x % 2 != 0, numeros))
print(num_impar)

# *Função reduce() tem que ser importada
# *sintexe:
# *reduce(função, sequência, valor_inicial)

from functools import reduce

def mult(x, y):
    return x * y

numeros = [1,2,3,4,5,6]

total = reduce(mult, numeros)
print(total)

#Soma cumulativa dos quadrados de valroes, usando expressão lambda
from functools import reduce

numeros = [1,2,3,4]
# ((1² + 2²)² + 3²)² + 4²

total = reduce(lambda x, y : x**2 + y**2, numeros )
print(total)