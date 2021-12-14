# 첫번째 데이터, 중간 데이터, 마지막 데이터 출력

n = int(input())
d = list(map(int, input().split()))

middle = int(n / 2)

print(d[0])
print(d[middle])
print(d[n - 1])
