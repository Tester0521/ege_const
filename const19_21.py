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
