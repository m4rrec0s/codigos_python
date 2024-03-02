# To-do List
from functions import *
from time import sleep

def space(ele, num):
    print(ele * num)


space('=', 20)
print('To-do List')
space('=', 20)

# nome do arquivo de txt gerado/aberto pelo programa
arq = 'todolist.txt'

# confere se o arquivo existe ou não
if not fileExists(arq):
    generateFile(arq)

name = input('What`s your name? => ')
age = input('What`s your age? => ')

space('=', 20)

print(f'Ok, {name}, let`s start!')

space('=', 20)


while True:
    print('Menu:')
    menu = int(input('''[1] => See full list.
[2] => Add new task.
[3] => Exit to program.

=> '''))

    space('=', 20)

    if menu == 1:
        openFile(arq)
        space('=', 20)

    elif menu == 2:
        print('Adicione novas tarefas:')
        nameTask = input('Name of the task: => ')
        space('=', 20)
        sleep(0.3)
        newtask = input('Describle the taks: => ')
        space('=', 20)
        sleep(0.3)
        time = int(input('Hours and Minutes: => '))
        space('=', 20)
        sleep(0.5)
        print('Ok, adding new tasks to the list.')
        space('=', 20)

        addTask(arq, nameTask, newtask, time)
        sleep(1)

    elif menu == 3:
        print('Até mais!')
        break

space('=',20)
