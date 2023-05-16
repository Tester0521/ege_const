# 5

al = '0123456789ABCDEFGHIJKLMNOP...'

n, n2 = 13, f'{bin(13)[2:]}'

for i in range(2):
    n2 = n2 + str( sum( list( map( int, list(n2) ) ) ) % 2 )

print(int(n2, 2))


# 8
from itertools import product as pr

al = ['А', 'В', 'С', 'Х']

reps = list(filter( lambda x: x.count('Х') == 1, \
                    [f'{el[0]}{el[1]}{el[2]}{el[3]}{el[-1]}' \
                    for el in pr(al, repeat = 5)] ))

print( len(reps) )

# 9
def xlsxToTxt(text: str = '9_.txt'):
    arr, arr2 = [], []
    with open(text) as t:
        for x in t.readlines():
            arr += x.split('\t')
        for el in arr:
            z = el.replace('\n', '')
            arr2.append(float(z.replace(',', '.')))
    return arr2

def main():
    mass = xlsxToTxt()
    cen =  round(sum(mass) / len(mass), 1)
    print(cen, min(mass))
    return len([i for i in mass if i < cen and i > min(mass)*2])

print(main())

# 12



s = '1'*99

while '111' in s:
    s = s.replace('111', '22', 1)
    s = s.replace('222', '11', 1)

print(s)

# 14


def base(x: int, y: int) -> str:
    al, res = '0123456789ABCDEFGHIJKLMNOPRST...', ''
    while x > 0:
        x, m = divmod(x, y)
        res += al[m]
    return res[::-1]

kk = base(4*625**9 - 25**15 + 2*5**11 - 7, 5)
print(kk, kk.count('4'))

# 15

def dd(x, y): return x % y == 0

for A in range(1, 1000-7):
    for x in range(1, 1000-7):
        if not((dd(x, 3) <= (not(dd(x, 5)))) or (x + A >= 90)): break
    else:
        print(A)
        break


        # 16 
from functools import lru_cache

@lru_cache(maxsize= 128)
def f(x):
    if x <= 2: return 2
    if x > 2: return 3 * f(x - 1) - f(x - 2)

print(f(100))

# 17

def _17_normal(path: str = './src/17.txt', c = 0, m = 0) -> list:
    s = [int(el) for el in open(path)]
    for x, x1 in enumerate(s[:-1]):
        for y, y1 in enumerate(s[x+1:]):
            if (x1 - y1) % 2 == 0 and (x1 % 19 == 0 or y1 % 19 == 0):
                c += 1
                m = max(m, x1 + y1)
    return [c, m]

# 19
def rocks(s, s2, h=1): # 24
    if ( h == 3 and s + s2 < 107 ) or ( h < 2 and s + s2 >= 107 ): return 0
    if h == 3 and s + s2 >= 107: return 1
    else: return rocks(s + 1, s2, h + 1) or rocks(s * 2, s2, h + 1) \
            or rocks(s, s2 + 1, h + 1) or rocks(s, s2 * 2, h + 1)

def rocks2(s, s2, h=1):
    if h == 4 and s + s2 < 107: return 0
    if h < 4 and s + s2 >= 107: return 0
    if h == 4 and s + s2 >= 107: return 1
    else:
        if h % 2 != 0: return rocks2(s + 1, s2, h + 1) or rocks2(s * 2, s2, h + 1) \
            or rocks2(s, s2 + 1, h + 1) or rocks2(s, s2 * 2, h + 1)
        else: return rocks2(s + 1, s2, h + 1) and rocks2(s * 2, s2, h + 1) \
            and rocks2(s, s2 + 1, h + 1) and rocks2(s, s2 * 2, h + 1)

def rocks3(s, s2, h=1):
    if h < 3 and s + s2 >= 107: return 0
    if h == 3 and s + s2 >= 107: return 1

    if h < 5 and s + s2 >= 107: return 0
    if h == 5 and s + s2 < 107: return 0
    if h == 5 and s + s2 >= 107: return 1
    else:
        if h % 2 == 0: return rocks3(s + 1, s2, h + 1) or rocks3(s * 2, s2, h + 1) \
            or rocks3(s, s2 + 1, h + 1) or rocks3(s, s2 * 2, h + 1)
        else: return rocks3(s + 1, s2, h + 1) and rocks3(s * 2, s2, h + 1) \
            and rocks3(s, s2 + 1, h + 1) and rocks3(s, s2 * 2, h + 1)


for i in range(1, 100):
    if rocks3(i, 13):
        print(i)




def rock(s1, s2=8, t=0):
    if (s1 + s2) >= 50 and t == 2: return 1
    elif (s1 + s2) < 50 and t == 2: return 0
    elif (s1 + s2 ) >= 50 and t < 2: return 0
    else:
        if t % 2 != 0: return rock(s1 + 1, s2, t + 1) or rock(s1 * 2, s2, t + 1) or rock(s1, s2 + 1, t + 1) or rock(s1, s2*2, t + 1)
        else: return rock(s1 + 1, s2, t + 1) or rock(s1 * 2, s2, t + 1) or rock(s1, s2 + 1, t + 1) or rock(s1, s2*2, t + 1)

def rock2(s1, s2=8, t=0):
    if (s1 + s2) >= 50 and t == 3: return 1
    elif (s1 + s2) < 50 and t == 3: return 0
    elif (s1 + s2 ) >= 50 and t < 3: return 0
    else:
        if t % 2 == 0: return rock2(s1 + 1, s2, t + 1) or rock2(s1 * 2, s2, t + 1) or rock2(s1, s2 + 1, t + 1) or rock2(s1, s2*2, t + 1)
        else: return rock2(s1 + 1, s2, t + 1) and rock2(s1 * 2, s2, t + 1) and rock2(s1, s2 + 1, t + 1) and rock2(s1, s2*2, t + 1)

def rock3(s1, s2=8, t=0):
    if (s1 + s2) >= 50 and (t == 4 or t == 2): return 1
    elif (s1 + s2) < 50 and t == 4: return 0
    elif (s1 + s2 ) >= 50 and t < 4: return 0
    else:
        if t % 2 != 0: return rock3(s1 + 1, s2, t + 1) or rock3(s1 * 2, s2, t + 1) or rock3(s1, s2 + 1, t + 1) or rock3(s1, s2*2, t + 1)
        else: return rock3(s1 + 1, s2, t + 1) and rock3(s1 * 2, s2, t + 1) and rock3(s1, s2 + 1, t + 1) and rock3(s1, s2*2, t + 1)

def rock31(s1, s2=8, t=0):
    if (s1 + s2) >= 50 and t == 2: return 1
    elif (s1 + s2) < 50 and t == 2: return 0
    elif (s1 + s2 ) >= 50 and t < 2: return 0
    else:
        if t % 2 != 0: return rock31(s1 + 1, s2, t + 1) or rock31(s1 * 2, s2, t + 1) or rock31(s1, s2 + 1, t + 1) or rock31(s1, s2*2, t + 1)
        else: return rock31(s1 + 1, s2, t + 1) or rock31(s1 * 2, s2, t + 1) or rock31(s1, s2 + 1, t + 1) or rock31(s1, s2*2, t + 1)


# 22
with open('../../downloads/22.csv') as f:
    arr = [el[:-1].split(',') for el in f.readlines()[1:]]
    dict = {'0': 0}
    for el in arr:
        key, time, follows = el[0], el[1], list(filter(lambda x: x != '', f'{el[-1]}'.split(';')))
        dict[key] = max([dict[i] for i in follows]) + int(time)
    print(dict)
    print(max(dict.values()))


# 23 
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


# 24 
def _24(s: str = open('./src/24.txt').readline(), f : str = 'XZZY'): return max([len(el) for el in s.split(f)])+(len(f)-1)*2

print(_24())


# 25
arr =[]

arr1 = [2**x for x in range(2, 28, 2)]
arr2 = [3**x for x in range(1, 25, 2)]

for x in arr1:
    for y in arr2:
        if 400_000_000 < x * y < 600_000_000:
            arr.append(x * y)

for elem in arr:
    print(elem)




# 26 
f = open('27880.txt')
s, n = map(int, f.readline().split())
v = sorted(map(int, f))
sum, cnt = 0, 0
　for i in range(len(v)):
　　if sum + v[i] <= s:
　　　sum += v[i]
　　　cnt += 1
biggest_file = v[cnt - 1:][0] + s - sum
while biggest_file not in v:
　biggest_file -= 1
print(cnt, biggest_file)



# 27
f=open('28130_B.txt')
n=int(f.readline())
numbers=[int(x) for x in f]
i=0
k=0
while i!=n:
    for h in range(i+1,n):
        if (numbers[i]+numbers[h])%80==0 and (numbers[i]>50 or numbers[h]>50):
            k=k+1
    i=i+1
print(k)