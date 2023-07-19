'''
The objective of this Python code is to creat a loop that will ask to user a name to append in a guest list.
The loop will run according to the number of guests that the user intends to invite.
'''
guestList=[]#An empty guest list
numberOfGuests=int(input("NUMBER OF GUESTS: "))#The number os guests

for i in range(numberOfGuests):#The for loop will repeat according to the range of numbers within the interval from 0 to numberOfGuests.
    guestName=input("GUEST NAME: ")#Ask the guest name
    guestList.append(guestName)#Add the guest name into the list

for name in guestList:#for each name in the guests list, print it
    if guestList.index(name)==0:
        print('\n'+name)
    else:
        print(name)
    