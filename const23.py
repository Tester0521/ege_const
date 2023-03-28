

def func(x = 1, y = 21):
    if x > y: return 0
    if x == y: return 1
    else: return func(x + 1, y) + func(x *  2, y)

print(func())