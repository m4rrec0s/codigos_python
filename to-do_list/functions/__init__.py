def generateFile(nome):
    try:
        with open(nome, 'wt+'):
            pass
    except Exception as e:
        print(f'Ocorreu um erro ao tentar criar o arquivo: {e}')
    else:
        print(f'-- Arquivo {nome} criado com sucesso! --')


def fileExists(nome):
    try:
        with open(nome, 'rt'):
            pass
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f'Ocorreu um erro ao verificar a existência do arquivo: {e}')
        return False
    else:
        return True


def openFile(nome):
    global a
    try:
        with open(nome, 'rt') as a:
            print('='*20)
            print('Suas Tarefas')
            print('='*20)
            print(a.read())
    except Exception as e:
        print(f'ERRO ao tentar ler o arquivo: {e}')


def addTask(arq, nameTask='<Undefined>', newtask='...', time=0):
    
    try:
        with open(arq, 'a') as a:
            a.write(f'{nameTask};{time}\n=> {newtask}\n')
    except Exception as e:
        print(f'Ouve um ERRO ao adicionar os dados: {e}')
    else:
        print(f'Cadastro de "{nameTask}" efetuado com sucesso!')
