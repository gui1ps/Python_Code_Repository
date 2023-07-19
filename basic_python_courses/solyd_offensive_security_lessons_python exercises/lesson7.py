'''
The objective of this Python code is to find both the smallest and the largest numbers in a list. It needs to print these found numbers.
'''

list_of_numbers=[-0.6,-0.5,0,1,2,3,4,5,6,7,102530]#List of numbers

def chooseTheLargest (list_num):#A function that will choose the largest number and return it.
    for num in list_num:
        if list_num.index(num)==0:#Firstly, the code will iterate over the list and take the item at position 0 up to the largest number value.
            largest=num

        if num>largest:#So, the value will be compared with the values of the other items. If a new largest value is found, the variable "value" will be changed.
            largest=num
    return largest

def chooseSmallestNumber (list_num):#This function will do exactly the same as the previous one, but with the opposite logic.
    for num in list_num:
        if list_num.index(num)==0:
            smallest=num

        if num<smallest:#the opposite logic is here.
            smallest=num
    return smallest

print(chooseTheLargest(list_of_numbers))
print(chooseSmallestNumber(list_of_numbers))
    
