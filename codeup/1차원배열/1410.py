# 올바른 괄호 1 (괄호 개수 세기)
s = input()

a = 0
b = 0

for i in range(len(s)):
    if s[i] == '(':
        a += 1
    elif s[i] == ')':
        b += 1

print(a, b)
