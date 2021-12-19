# C언어를 찾아라

# 'c' , 'cc'가 암호문의 몇 개 있는지 출력(대소문자 구분없음)

s = input()
c = 0
cc = 0

for i in range(2):
    if i == 0:
        for j in range(len(s)):
            if s[j] == 'c' or s[j] == 'C':
                c += 1
        print(c)
    else:
        for j in range(len(s) - 1):
            if s[j] == 'c' and s[j + 1] == 'c':
                cc += 1
            elif s[j] == 'c' and s[j + 1] == 'C':
                cc += 1
            elif s[j] == 'C' and s[j + 1] == 'c':
                cc += 1
            elif s[j] == 'C' and s[j + 1] == 'C':
                cc += 1
        print(cc)
