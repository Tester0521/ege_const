

def f(x):
    if x <= 2: return 2
    if x > 2: return 3 * f(x - 1) - f(x - 2)

print(f(6))