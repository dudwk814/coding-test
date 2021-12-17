# 30분전
h, m = map(int, input().split())  # h = 시간, m = 분

if m > 30:  # m이 30보다 크다면 m에서 30을 빼고 결과 출력
    print(h, (m - 30), sep=' ')
elif m == 30:   # m이 30이라면 m에서 30을 빼고 결과 출력
    m -= 30
    print(h, m, sep=' ')
else:   # m이 30보다 작으면 h를 -1하고, m = 60 + (m - 30)하고 결과 출력
    m = 60 + (m - 30)
    if h > 0:
        h -= 1
    else:
        h = 24 + (h - 1)
    print(h, m, sep=' ')
