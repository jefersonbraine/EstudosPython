# Funções buil in (internas)

valores = [2,5,6,7,-9,0,11,56,78]
print(max(valores))#maior valor
print(min(valores))#menor valor

a = -5
b = 4

#valor absoluto
print(abs(a))

#exponenciaçào
print(pow(a, b))

#arredondamento
c = 2.789111
print(round(c, 2))#valor, número de casas decimais

#Módulo math

import math

x = 8
y = 100

raiz_quadrada = math.sqrt(x)
print(math.ceil(raiz_quadrada))#arredonda o valor pra cima
print(math.floor(raiz_quadrada))#arredonda o valor pra baixo
print(round(raiz_quadrada, 2))#arredondar

logaritmo = math.log10(y)
print(logaritmo)

print(math.pi)
print(math.factorial(y))#fatorial
print(x / math.inf)#infinito