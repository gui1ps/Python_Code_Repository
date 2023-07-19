import sys
import os

#O objetivo deste código e criar uma ferramente que consiga listar todos as pastas existente em um computador com base num path inicial. O software faz uma varredura completa até não encontrar mais pastas para mostrar

#Função que analisa todos os diretorios dentro de um caminho e os diretorios dos diretiorios encontratodos no caminho inicial de forma recursiva
def analisa_dir(caminho):
    caminho=os.path.normpath(os.path.normcase(caminho))
    raiz=caminho #cria uma cópia do caminho inicial para ser utilizada junto com a  função join na linha 11, com a finalidade de criar novos caminhos (pensado para ser usado recursivamente) 
    if os.path.lexists(caminho): #analisa se o caminho realmente existe no sistema. caso não exista, será printado "Caminho inexistente"
        dirs=os.listdir(caminho) #cria uma variável no formato de lista com todos o diretórios do caminho indicado
        for d in dirs:
            caminho=os.path.join(raiz,d) #para cada diretório encontrado na listagem, elabora o caminho do diretorio unindo o nome dele com a cópia do caminho inicial criada
            if os.path.isdir(caminho): #por via de dúvidas, analisa se o caminho elaborado realmente se trata de um diretótio no sistema
                print(caminho)
                analisa_dir(caminho)  #chama a função de forma recursiva para analisar os diretórios dentro dos diretórios encontrados
            else:
                pass
    else:
        print('Caminho inexistente')


argumentos=sys.argv #atribui os argumentos passados para o programa na variável argumentos através da api sys do sistema

if os.path.lexists(argumentos[1]): #condicional que vai avaliar se o caminho passado como argumento existe. caso exista, vai executar a função analisa_dir
    analisa_dir(argumentos[1])
    