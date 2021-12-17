# 홀수와 짝수 그리고 더하기

a, b = map(int, input().split())

if a % 2 != 0:
    if b % 2 != 0:
        print('홀수+홀수=짝수')
    else:
        print('홀수+짝수=홀수')
elif a % 2 == 0:
    if b % 2 != 0:
        print('짝수+홀수=홀수')
    else:
        print('짝수+짝수=짝수')
