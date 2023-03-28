

def dd(x, y): return x % y == 0

for A in range(1, 1000-7):
    for x in range(1, 1000-7):
        if not((dd(x, 3) <= (not(dd(x, 5)))) or (x + A >= 90)): break
    else:
        print(A)
        break