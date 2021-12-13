# 기부
k, h = map(int, input().split())


if k % 2 != 0:  # k가 홀 수일 경우
    d = 0
    for i in range(1, k + 1):
        if i % 2 != 0:
            d += 1
    k = d
else:  # k가 짝 수일 경우
    k = (k * 10) / 2

if h % 2 != 0:  # h가 홀 수일 경우
    d = 0
    for i in range(1, h + 1):
        if i % 2 != 0:
            d += 1
    h = d
else:  # h가 짝 수일 경우
    h = (h * 10) / 2

print(int(k + h))
