'''
The objective of this Python code is to create a form containing the user's name, age, height, and weight.
Then, the code should analyze this information and decide if the user is eligible to join the army.
The parameters to determine eligibility are that the age must be over 18, the weight must be equal to or greater than 60kg, and the height must be greater than 1.70 meters.
'''

def iseligible(age,height,weight):#A function that takes the user's inputs and will return True or False if the user is eligible
    if age>=18:
        if height>1.70:
            if weight>=60:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


#The user's inputs
name=input("NAME: ")
age=int(input("AGE: "))
height=float(input("HEIGHT: "))
weight=float(input("WEIGHT: "))


if iseligible(age,height,weight):
    print(f'{name} is eligible')
else:
    print(f'{name} is not eligible')
