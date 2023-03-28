arr, result = [], []

arr1 = [[2**x, x] for x in range(28)]
arr2 = [[3**x, x] for x in range(25)]

for x in arr1:
    for y in arr2:
        if 400_000_000 < x[0] * y[0] < 600_000_000:
            arr.append(f'2^{x[-1]} * 3^{y[-1]} == {x[0] * y[0]}')
            result.append(x[0] * y[0])

print(arr)
print(f'result: {sorted(result)}')