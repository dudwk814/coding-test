n = int(input())

dic = {}

for i in range(n):
    book = input()

    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 1

array = list(dic.items())
array.sort(key=lambda x: (-x[1], x[0]))
print(array[0][0])
