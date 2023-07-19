'''
The objective of these Python code is to create a form containing the user's name, identification, address, height, and phone number. 
Then, the code should print the information on the screen in an organized manner.

'''
def createReport(name,id,addr,height,pn): #A function that takes parameters for name, address, height, and phone number.
    return f'''
    NAME: {name}
    ID: {id}
    ADDRESS:{addr}
    HEIGHT: {height}
    PHONE NUMBER: {pn}
    '''
    #It will return a string that takes these parameters and adds them to the text.

#The user's inputs
name=input("NAME: ")
id=input("ID: ")
addr=input("ADDRESS: ")
height=float(input("HEIGHT: "))
pn=input("PHONE NUMBER: ")


print(createReport(name,id,addr,height,pn))
