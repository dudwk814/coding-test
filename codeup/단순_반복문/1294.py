# 시저의 암호2
# 입력받은 평문의 아스키코드의 +3이 적용됨
s = input()
w = ""
list = []
for i in range(len(s)):

    if s[i] == " ":
        list.append(w)
        w = ""
        continue

    if i == len(s) - 1:
        w = w + chr(ord(s[i]) + 3)
        list.append(w)
        break

    if s[i] == 'x':
        w = w + 'a'
    elif s[i] == 'y':
        w = w + 'b'
    elif s[i] == 'z':
        w = w + 'c'
    else:
        w = w + chr(ord(s[i]) + 3)

    # print(chr(ord(s[i]) + 3))

for i in range(len(list)):
    print(list[i], end=' ')
