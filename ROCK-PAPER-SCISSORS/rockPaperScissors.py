from time import sleep
import random

randomn=['Pedra','Papel', 'Tesoura']
maquina=0
nomemaquina='BOT'
usr=str(input('Escolha um nome de usuário : '))

while True:
    escolha=str(input('Escolha: 0-PEDRA, 1-PAPEL, 2-TESOURA:  '))

    if escolha=='0':
        print('Pedra selecionada!')
        escolha='Pedra'
        break

    elif escolha=='1':
        print('Papel selecionado!')
        escolha='Papel'
        break
    elif escolha=='2':
        print('Tesoura selecionada!')
        escolha='Tesoura'
        break
    else:
        print('Valor inválido!')
        continue

sleep(1)
print('Hora de jogar!')

sleep(1)
print('TRÊS!')
sleep(1)
print('DOIS!')
sleep(1)
print('UM!')
sleep(1)

maquina=randomn[random.randrange(0,3)]
print('A máquina jogou:  '+ maquina)

while True:

    if escolha=='Pedra' and maquina=='Papel':
        print('Você perdeu!')
        print(usr +': '+escolha+' X '+ maquina+' : '+nomemaquina )
        break
    elif escolha=='Pedra' and maquina=='Tesoura':
        print('Você ganhou!')
        print(usr +': '+escolha+' X '+ maquina+' : '+nomemaquina )
        break
    elif escolha=='Papel' and maquina=='Tesoura':
        print('Você perdeu!')
        print(usr +': '+escolha+' X '+ maquina+' : '+nomemaquina )
        break
    elif escolha=='Papel' and maquina=='Pedra':
        print('Você ganhou!')
        print(usr +': '+escolha+' X '+ maquina+' : '+nomemaquina )
        break
    elif escolha=='Tesoura' and maquina=='Papel':
        print('Você ganhou!')
        print(usr +': '+escolha+' X '+ maquina+' : '+nomemaquina )
        break
    elif escolha=='Tesoura' and maquina=='Pedra':
        print('Você Perdeu!')
        print(usr +': '+escolha+' X '+ maquina+' : '+nomemaquina )
        break
    elif escolha==maquina:
        print ('Empate -> '+ usr +': '+escolha+' X '+ maquina+' : '+nomemaquina)
        break
    