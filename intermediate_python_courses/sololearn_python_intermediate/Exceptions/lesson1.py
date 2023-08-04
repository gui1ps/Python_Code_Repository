def withdraw(amount):
   print(str(amount) + " withdrawn!")

try:
   x=int(input())
   withdraw(x)
except ValueError:
   print('Please enter a number')

