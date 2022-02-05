from array import array


n = int(input())
array = []

no_array = []
for i in range(n):
    c, no, name = input().split()

    if c == 'I':
        if not int(no) in no_array:
            array.append((int(no), name))
            no_array.append(int(no))
    else:
        if int(no) in no_array:
            for value in array:
                if value[0] == int(no):
                    array.remove(value)
                    no_array.remove(int(no))

order = list((map(int, input().split())))
array.sort(key=lambda x: x[0])

for i in order:
    print(array[i - 1][0], array[i - 1][1])
