# 5개의 정수들의 최댓값과 최솟값을 구하는 프로그램을 작성

d = []
max = 0
min = 0

for i in range(5):  # 5개의 정수 입력받기
    d.append(int(input()))

for i in range(len(d) - 1):
    if i == 0:  # 처음 루프에 max, min값 초기화
        max = d[i]
        min = d[i]

    if max < d[i + 1]:  # 현재 max값 보다 다음 리스트의 값이 크다면 스왑
        max = d[i + 1]

    if min > d[i + 1]:  # 현재 min 값보다 다음 리스트의 값이 작다면 스왑
        min = d[i + 1]

print(max)
print(min)
