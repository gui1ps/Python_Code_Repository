from time import sleep
from randword import rword

print(f'''
{16*'_-'}

BEM VINDO AO JOGO DA FORCA

{16*'_-'}
''')

sleep(2)

while True:
    quest=input('Iniciar novo jogo?[s/n]')
    if quest.lower()=='n':exit()
    elif quest.lower()=='s':

        conter=-1
        contador_erros=0
        word=rword('Teste')
        word_value=word.word.lower()
        enpty_list=[]
        play=True

        for l in word_value:
            enpty_list.append('_')
        
        print(word_value)

        while play:

            chute=input('Chute uma letra: ')
            
            if chute in word_value:
                for l in word_value:
                    conter+=1
                    if l==chute:
                        enpty_list[conter]=l
            else:
                 contador_erros+=1

            if contador_erros==1:
                        print(' O')
            elif contador_erros==2:
                       print('''    
                             O
                             |''') 
            elif contador_erros==3:
                       print(u'''    
                             O
                             |
                            \u2571 ''')
            elif contador_erros==4:
                       print(u'''    
                             O
                             |
                            \u2571 \u2572''')   
            elif contador_erros==5:
                       print(u'''    
                             O
                            -
                             |
                            \u2571 \u2572''')  
            elif contador_erros==6:
                       print(u'''    
                             O
                            - -
                             |
                            \u2571 \u2572''')       
                       play=False     
            conter=-1
            print(enpty_list)

    else:continue