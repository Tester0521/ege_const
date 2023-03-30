f = open('./24.txt').readline()
f = f.replace('L', 'x')
f = f.replace('R', 'x')
arr = f.split('x')

print(len(max(arr)))