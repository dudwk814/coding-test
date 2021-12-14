# 식을 입력하면 차례대로 계산하여 출력하는 계산기
d = input()
s = ""
list = []
r = 0
operator = 0
for i in range(len(d)):
    if d[i] == '+':

        list.append(s)
        list.append(d[i])
        s = ""
    elif d[i] == '-':

        list.append(s)
        list.append(d[i])
        s = ""
    elif d[i] == '*':

        list.append(s)
        list.append(d[i])
        s = ""
    elif d[i] == '/':
        list.append(s)
        list.append(d[i])
        s = ""
    elif d[i] == '=':

        list.append(s)
        list.append(d[i])
        s = ""
    else:
        s += d[i]

for i in range(len(list)):
    if i == 0:
        r += int(list[i])

    elif list[i] == '+':
        r = int(int(r) + int(list[i + 1]))

    elif list[i] == '-':
        r = int(int(r) - int(list[i + 1]))

    elif list[i] == '*':
        r = int(int(r) * int(list[i + 1]))

    elif list[i] == '/':
        r = int(int(r) / int(list[i + 1]))

    elif list[i] == '=':
        print(int(r))
