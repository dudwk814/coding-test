# 당신의 사주를 봐 드립니다 2

y, m, d = map(int, input().split())
result = str(y + m + d)
result = int(result[len(result) - 3])

if result % 2 == 0:
    print('대박')
else:
    print('그럭저럭')
