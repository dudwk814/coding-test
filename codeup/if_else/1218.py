# 삼각형 판단하기

a, b, c = map(int, input().split())
list = [a, b, c]
list.sort()

if c < a + b:
    if a == b and b == c:
        print('정삼각형')
    elif (a == b and a != c) or (b == c and a != b):
        print('이등변삼각형')
    elif a**2 + b**2 == c**2:
        print('직각삼각형')
    else:
        print('삼각형')
else:
    print('삼각형아님')
