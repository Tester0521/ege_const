with open('../../downloads/22.csv') as f:
    arr = [el[:-1].split(',') for el in f.readlines()[1:]]
    dict = {'0': 0}
    for el in arr:
        key, time, follows = el[0], el[1], list(filter(lambda x: x != '', f'{el[-1]}'.split(';')))
        dict[key] = max([dict[i] for i in follows]) + int(time)
    print(dict)
    print(max(dict.values()))