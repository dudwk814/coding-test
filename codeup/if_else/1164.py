# 터널 통과하기 1

n = list(map(int, input().split()))

for i in range(len(n)):
    if n[i] <= 170:
        print("CRASH")
        break
    elif i == len(n) - 1:
        print('PASS')
