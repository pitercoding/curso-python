from ex115.lib.interface import *
from time import sleep
while True:
    resposta = menu(['Criar Arquivo', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('\033[32mArquivo\033[m')
    elif resposta == 2:
        cabeçalho('\033[32mPessoa\033[m')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(1)