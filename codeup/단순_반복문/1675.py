# 시저의 암호1
# 입력받은 암호문의 아스키코드에 -3이 적용됨
s = input()
w = ""
list = []
for i in range(len(s)):

    if s[i] == " ":
        list.append(w)
        w = ""
        continue

    if i == len(s) - 1:
        w = w + chr(ord(s[i]) - 3)
        list.append(w)
        break

    if s[i] == 'a':
        w = w + 'x'
    elif s[i] == 'b':
        w = w + 'y'
    elif s[i] == 'c':
        w = w + 'z'
    else:
        w = w + chr(ord(s[i]) - 3)

    # print(chr(ord(s[i]) + 3))

for i in range(len(list)):
    print(list[i], end=' ')
