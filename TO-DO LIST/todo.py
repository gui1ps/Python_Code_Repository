import os
import datetime
from time import sleep
from tabulate import tabulate
import keyboard

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

taskList=[]

def showOptions():
    try:
        clear_terminal()
        option=int(input(f"""
                        
                Olá, bem vindo(a) a lista de tarefas!
                Menu de opções:
                
                1)Visualizar tarefas
                2)Adicionar uma nova tarefa
                3)Editar uma tarefa
                4)Remover uma tarefa
                5)Sair
                
            """))
        return option
    except ValueError:
        print('Valor inválido, tente novamente!')
    
def viewTasks(exit_key=False):
    clear_terminal()
    if len(taskList) > 0:
        dadosTbela = []
        for index, task in enumerate(taskList):
            dadosTbela.append([
                index,
                task.get('titulo', 'N/A').upper(),
                task.get('descricao', 'N/A'),
                task.get('prazo', 'N/A'),
            ])
        
        headers = ["#", "Título", "Descrição", "Prazo"]
        print(tabulate(dadosTbela, headers=headers, tablefmt="grid"))
        if exit_key:
            print('Pressione "Esc" para voltar...')
            while True:
                event = keyboard.read_event()
                if event.name == 'esc' and event.event_type == keyboard.KEY_DOWN:
                    break
        return True
    else:
        print('Nenhuma tarefa foi encontrada.')
        if exit_key:
            print('Pressione "Esc" para voltar...')
            while True:
                event = keyboard.read_event()
                if event.name == 'esc' and event.event_type == keyboard.KEY_DOWN:
                    break  
        return False


def verificarPrazo():
    while True:
        data=input('Prazo  (AAAA-MM-DD): ')
        try:
            data=datetime.datetime.strptime(data, "%Y-%m-%d")
            return data
        except ValueError:
            print(f'A data {data} não é válida')
            continue
             
def addTask():
    clear_terminal()
    novaTask={}
    novaTask.update({'titulo':input('Título: ')})
    novaTask.update({'descricao':input('Descrição: ')})
    novaTask.update({'prazo':verificarPrazo()})
    taskList.append(novaTask)
    
def selectTask(acao):
    while True:
        try:
            resposta=int(input(f'Qual tarefa você deseja selecionar para {acao}? > '))
        except ValueError:
            print('Valor incorreto, tente novamente!')
            continue
        if resposta >=0 and resposta <=len(taskList)-1:
            taskSelecionada=taskList[resposta]
            return (resposta,taskSelecionada)
        else:
            print('Valor incorreto, tente novamente!')
            continue
            
def editTask():
    clear_terminal()
    if viewTasks():
        taskSelecionada=selectTask('editar')
        novaTask={}
        print("## MODO EDIÇÃO ##\n")
        novaTask.update({'titulo':input(f'Título antigo: {taskSelecionada[1].get("titulo")} | Título novo: ')})
        novaTask.update({'descricao':input(F'Descrição antiga: {taskSelecionada[1].get("descricao")} | Descrição nova: ')})
        novaTask.update({'prazo':verificarPrazo()})
        taskList[taskSelecionada[0]]=novaTask
        print("Dados gravados com sucesso!")
           
def deleteTask():
    clear_terminal()
    if viewTasks():
        taskSelecionada=selectTask('excluir')
        tarefaRemovida=taskList.pop(taskSelecionada[0])
        print(f'A tarefa "{tarefaRemovida.get("titulo")}" foi removida com sucesso!')

def choose(option):
    match option:
        case 1:
            viewTasks(exit_key=True)
        case 2:
            addTask()
        case 3: 
            editTask()
        case 4:
            deleteTask()  
        case 5:
            print('Saindo...')
            sleep(2)
            exit()
        case _:
            print('Opção inválida, tente novamente!')
    
if __name__ == '__main__':
    while True:
        choose(showOptions())
