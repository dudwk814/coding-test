n = input()
value = 0
result = 0
for i in range(1, int(n) + 1):
    str_i = str(i)
    result = i
    value = i
    for i in range(len(str_i)):
        value += int(str_i[i])

    if value == int(n):
        break

if value == int(n):
    print(result)
else:
    print(0)    
