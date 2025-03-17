# Exceção - representa um erro que ocorreu ao executar o programa.

# Bloco try ... except

def div(k, j):
    return round(k / j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite outro número: '))
            break
        except ValueError:
            print(f'Ocorreu um erro ao ler o valor. Tente novamente.')

    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print(f'Não é possivel dividir por zero!')
    except: 
        print(f'Ocorreu um erro desconhecido...')
    else:
        print(f'resultado: {r}')
    finally:
        print(f'\n Fim do cálculo')







# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))


# try: 
#     r = round (n1 / n2, 2)
# except ZeroDivisionError:
#     print(f'Não é possivel dividir por zero!')
# else:
#     print(f'resultado: {r}')