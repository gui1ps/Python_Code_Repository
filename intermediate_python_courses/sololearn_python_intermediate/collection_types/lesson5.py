def calc(x):
    return x*4,x*x
    
side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))