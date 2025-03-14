bebida = input('Digite suas cinco bebidas favoritas: ')

lista = bebida.split(f'\s')
lista.sort()

for bebida in lista:
    print(bebida.strip())