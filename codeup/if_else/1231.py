# 계산기 1

s = input()

if s.find('+') > 0:
    a, b = map(int, s.split('+'))
    print(a + b)
elif s.find('-') > 0:
    a, b = map(int, s.split('-'))
    print(a - b)
elif s.find('*') > 0:
    a, b = map(int, s.split('*'))
    print(a * b)
elif s.find('/') > 0:
    a, b = map(int, s.split('/'))
    result = a / b
    print("%.2f" % result)
