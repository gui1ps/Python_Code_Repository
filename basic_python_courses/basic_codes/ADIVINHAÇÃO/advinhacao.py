import random
import user
import randomnumber
from time import sleep
#P29
print('''
*******************************************
*                WELCOME                  *
*******************************************
          ''')

while True:
    qst=input('Iniciar novo jogo? [s/n]')

    if qst=='s': iniciar=True;user_name=input('Nome de usuário: ');user1=user.User(user_name);sleep(1);print('Usuário criado!');print(user1.__str__())
    elif qst=='n':exit()
    else: print('Resposta não conhecida');continue

    print('>:>:> LEMBRE-SE: VOCÊ TEM APENAS 3 CHANCES <:<:<')

    while iniciar:
        sleep(1)
        number=randomnumber.NumberForGame()
        print(f'>>>>> o seu número fica entre {number.dardicadificil()[0]} e {number.dardicadificil()[1]} <<<<<')
        sleep(0.25)
        x=int(input('Chute: '))

        if x==number.value:
            print('Você acertou!')
            print('FIM DE JOGO')
            user1.add_point()
            print(user1.__str__())
            break
        else:
            print('Você errou!')
            user1.sub_point()
            print(f'O seu número fica mais próximo de: {number.dardicamedia()}')
            x=int(input('Chute: '))
            if x==number.value:
                print('Você acertou!')
                print('FIM DE JOGO')
                user1.add_point()
                print(user1.__str__())
                break
            else:
                print('Você errou!')
                print(f'O seu número fica muito próximo de: {number.dardicafacil()}')
                x=int(input('Chute: '))
                if x==number.value:
                    print('Você acertou!')
                    print('FIM DE JOGO')
                    user1.add_point()
                    print(user1.__str__())
                    break
                else:
                    print('Você perdeu todas as chances!')
                    print(f'O número correto era: {number.value}')
                    
        print(user1.__str__())
        break
