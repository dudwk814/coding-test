from types import resolve_bases


n, k = map(int, input().split())  # n = 배열의 크기, k = 바꿔치기 횟수
array1 = list(map(int, input().split()))  # a 배열
array2 = list(map(int, input().split()))  # b 배열

a = sorted(array1)
b = sorted(array2, reverse=True)

for i in range(k):
    if a[i] < b[i]: # a배열에서 가장 작은 값이 b배열에서 가장 큰 값보다 작다면
        a[i], b[i] = b[i], a[i] # 스왑

print(sum(a))
