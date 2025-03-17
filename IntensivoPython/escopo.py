#Escopo Global e Local

var_global = 'Curso de Python'

def escreve_texto():
    global var_global #para alterar a variável global(se referir a variável global, atribuindo a externa)
    var_global = 'Bancos de dados com SQL'
    var_local = 'Fábio'
    print(f'Variável Global: { var_global}')
    print(f'Variável Local: { var_local}')

if __name__ == '__main__':
    print(f'Executar a função escreve_texto()')
    escreve_texto()

    print('Tentar acessar as variaveis diretamente')
    print(f'Variável Global: { var_global}')