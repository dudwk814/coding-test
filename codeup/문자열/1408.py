# 암호처리

# 입력받은 문자의 ASCII 코드값 + 2
# (입력받은 문자의 ASCII 코드값 * 7) % 80 + 48

s = input()

for i in range(2):
    if i == 0:
        for j in range(len(s)):
            c = chr(ord(s[j]) + 2)
            print(c, end='')
    else:
        for j in range(len(s)):
            c = chr((ord(s[j]) * 7) % 80 + 48)
            print(c, end='')
    print()
