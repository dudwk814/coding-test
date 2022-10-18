array = list(map(int, input().split()))
eq = False

for i in range(len(array)):
    if array.count(array[i]) == 3:
        print(array[i] * 1000 + 10000)
        break
    elif array.count(array[i]) == 2:
        print(array[i] * 100 + 1000)
        break
    else:
        if i == 2:
            eq = True

if eq:
    print(max(array) * 100)
