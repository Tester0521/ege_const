al = '0123456789ABCDEFGHIJKLMNOP...'

n, n2 = 13, f'{bin(13)[2:]}'

for i in range(2):
    n2 = n2 + str( sum( list( map( int, list(n2) ) ) ) % 2 )

print(int(n2, 2))
