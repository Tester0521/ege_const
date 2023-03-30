

def func(x = 1, y = 21):
    if x > y: return 0
    if x == y: return 1
    else: return func(x + 1, y) + func(x *  2, y)

print(func())



# на пути не должно быть 47 и должно быть 12

def f(x, y):
    if x > y or x == 47: return 0
    if x == y: return 1
    else: return f(x+1, y) + f(x*2, y)

print(f(2, 12) * f(12, 50))
