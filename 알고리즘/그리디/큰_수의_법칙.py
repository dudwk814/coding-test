# n = 배열의 크기, m = 더하기 횟수, k = 한 인덱스를 연속해서 더 더할 수 있는 횟수
n, m, k = map(int, input().split())

list = list(map(int, input().split()))

list.sort(reverse=True)  # 리스트를 내림차순으로 정렬

k = 0   # 특정 인덱스의 값을 더한 횟수
s = 0   # 인덱스들을 더한 값
# for i in range(m):
#     if k == 3:
#         s += list[1]
#         k = 0
#         continue
#     s += list[0]
#     k += 1

# print(s)

# 가장 큰 수가 더해지는 횟수
count = int(m / (k + 1)) * k
count += m % (k + 1)

s += (count) * list[0]  # 가장 큰수가 더해지는 횟수 * 가장 큰수
s += (m - count) * list[1]  # 전체 더하기 횟수에서 가장 큰수가 더해지는 횟수를 뺀 결과 * 두 번째로 큰 수


print(s)
