t = int(input())

for _ in range(t):
    array = list(input().split())

    for i in range(len(array)):
        w = array[i][::-1]

        array[i] = w

        print(array[i], end=' ')

    print()
