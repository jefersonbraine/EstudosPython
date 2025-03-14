x = y = z = False
n1 = n2 = 0

print('Digite um número: ')
n1 = int(input())
n2 = int(input('Digite outro número: '))

x = n1 == n2
print('São iguais? ', x, '\n')

z = n1 > n2
print(n1, ' é maior que ', n2, '? ', z, '\n')


y = n1 != n2
print('São diferentes? ' + str(y)) #Se deixar apenas o y aparece que não pode concatenar bool apenas str