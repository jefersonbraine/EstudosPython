
#* Simples, Composto, Encadeado

#* Simples
n1 = n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

#* calcular a media aritmética das notas
media = (n1 + n2) / 2 

if (media >= 7):
    print("Resultado: Aprovado") #se for verdadeiro
elif (media >= 5):
    print('Em recuperação')
else:
    print('Reprovado')

print('Sua média é {}'.format(media))