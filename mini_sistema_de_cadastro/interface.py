# importação de funções criadas em pacotes separados
import funcoes
import arquivo
from time import sleep

# nome do arquivo de txt gerado/aberto pelo programa
arq = 'pessoas_cadastradas.txt'

# confere se o arquivo existe ou não
if not arquivo.arquivoExiste(arq):
    arquivo.gerarArquivo(arq)

# loop que deixa o menu ativo até o usuário decidir sair
while True:
    opc = funcoes.menu(['Ver pessoas cadastradas',
                        'cadastrar nova pessoa',
                         'Sair do programa'])

    sleep(0.5)
    if opc == 1:
        arquivo.lerArquivo(arq)

    elif opc == 2:
        n = str(input('Nome: ')).title()
        i = funcoes.leiaInt('Idade: ')
        arquivo.AdcionarPessoa(arq, n, i)

    elif opc == 3:
        funcoes.cabecalho(f'{funcoes.cores[1]}   \t{"SAINDO DO PROGRAMA"} {funcoes.cores[0]}')
        break
    else:
        print('\033[31mERRO! opção não encontrada!\033[m')
    sleep(1)
