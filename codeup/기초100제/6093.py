n = int(input())    # 번호를 부른 횟수
a = input().split()  # n만큼의 번호가 공백을 두고 입력됨

for i in range(n):
    a[i] = int(a[i])

for i in range(n - 1, -1, -1):  # n - 1부터 0까지 -1씩 감소하며 루프
    print(a[i], end=' ')
