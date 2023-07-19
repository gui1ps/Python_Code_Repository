'''
This code will simulate an ATM login. The ATM that I've taken as an example has an authentication method that includes the following login-password format:
There are four buttons, each with two numbers. Example:

BTN1) 1 AND 2
BTN2) 3 AND 4
BTN3) 5 AND 6
BTN4) 7 AND 8

The user's password has 6 characters. So, for each character, if the character value exists in any button, the button must be pressed.
So, if the user's password is 341762 (example), the user needs to press the following buttons: 2-2-1-4-3-1 to loggin
'''
from clientss import clients 

btns={'1':('1','2'),'2':('3','4'),'3':('5','6'),'4':('7','8')}

c1=clients('Lucas','341762')

def loggin(cliente):

    print('''
    BTN1) 1 AND 2
    BTN2) 3 AND 4
    BTN3) 5 AND 6
    BTN4) 7 AND 8
    ''')

    cliente_password=str(cliente.getPass())
    print(cliente_password)
    
    for char in cliente_password:
        btn=input('BUTTON: ')

        if int(btn)<1 or int(btn)>4:
            print("INVALID BUTTON")
            continue
        else:
            if btns[btn][0]==char or btns[btn][1]==char:
                print("CORRECT")
            else:
                print("FAIL")
    
loggin(c1)