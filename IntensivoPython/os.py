#Exemplo

import os

os.chdir('c:\\test')
print(f'Diretório atual: { os.getcwd()}')

padrao_nome = input('Qual o padrão de nomes de arquivos a usar (sem a extensão)?')

for contador, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = padrao_nome + ' ' + str(contador)

        nome_novo = f'{nome_arq}{exten_arq}'
        os.rename(arq, nome_novo)

print(f'\n Arquivos renomeados.')