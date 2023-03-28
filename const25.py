arr =[]

arr1 = [2**x for x in range(2, 28, 2)]
arr2 = [3**x for x in range(1, 25, 2)]

for x in arr1:
    for y in arr2:
        if 400_000_000 < x * y < 600_000_000:
            arr.append(x * y)

print(arr)