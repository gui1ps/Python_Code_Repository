menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']

try:
    x=int(input())
    print(menu[x])
except:
    print('Item not found')
else:
    print('Thanks for your order')