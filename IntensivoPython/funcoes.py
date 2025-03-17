# Funções = bloco de codigo
# Modularização, reúso de código, legibilidade
# funções internas e definidas pelos usuários


# def <nome_função> ([argumentos]):
#     <instruções>

def mensagem():
    print('Bóson de Higgs')
    print('Curso completo de Python')

mensagem()


#Função com argumentos

def soma(a, b):
    print(a + b)

soma (10, 20)

#return

def mult(x, y):
    return x * y

a = 5
b = 8
c = mult(a, b)
print(f'O produto de {a} e {b} é {c}')


def div(k, j):
    if j !=0:
        return k / j
    else:
        return 'Impossivel dividir por zero!'

if __name__ == '__main__':
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))

    r = div(a, b)
    print(f'{a} dividido por {b} é igual a {r}')


def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
    return quadrados

if __name__ == '__main__':
    valores = [2,5,7,9,12]
    resultados = quadrado(valores)
    for g in resultados:
        print(g)


# * PARAMETROS OPCIONAIS

# def contar(num=11, caractere='+'):
#     for i in range(1, num):
#         print(caractere)

# if __name__ == '__main__':
#     # contar(caractere='&')#troca o caractere
#     # contar(num=8, caractere='@') #muda a quantidade de linhas e o caractere
#     contar(6, '@')


# def contar(caractere, num=11): #se deixar sem nada precisa colocar ele primeiro
#     for i in range(1, num):
#         print(caractere)

# if __name__ == '__main__':
#    contar('@', 3)
#    contar(num=3, caractere='#') #se nomeado a ordem não importa tanto

x = 5
y = 6
z = 3

def soma_mult(a, b, c = 0):
    if c == 0:
        return a * b
    else:
        return a + b + c

if __name__ == '__main__':
    res = soma_mult(x, y, z)
    print(res)
