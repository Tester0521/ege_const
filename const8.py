from itertools import product as pr

al = ['А', 'В', 'С', 'Х']

reps = list(filter( lambda x: x.count('Х') == 1, \
                    [f'{el[0]}{el[1]}{el[2]}{el[3]}{el[-1]}' \
                    for el in pr(al, repeat = 5)] ))

print( len(reps) )


