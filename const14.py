

def base(x: int, y: int) -> str:
    al, res = '0123456789ABCDEFGHIJKLMNOPRST...', ''
    while x > 0:
        x, m = divmod(x, y)
        res += al[m]
    return res[::-1]

kk = base(4*625**9 - 25**15 + 2*5**11 - 7, 5)
print(kk, kk.count('4'))