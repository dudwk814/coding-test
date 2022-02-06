import sys
n = int(input())
no_array = []
array = []

for i in range(n):
    c, no, name = sys.stdin.readline().split()
    no = int(no)
    if c == 'I':
        array.append((no, name, i))
        no_array.append(no)

    else:  # c값이 D라면

        d = []
        for i in range(len(array)):
            if array[i][0] == no:
                d.append(array[i])
        if len(d) != 0:
            array.remove(d[len(d) - 1])

array.sort(key=lambda x: (x[0], -x[2]))  # 다음 들어올 값을 위해 오름차순 정렬
order = [x for x in map(int, input().split())]

for i in order:
    print(array[i - 1][0], array[i - 1][1])
