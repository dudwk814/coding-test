n = int(input())
array = list(map(int, input().split()))
m = int(input())

# 2진 탐색을 위한 시작과 끝점
start = 0
end = max(array)

if sum(array) <= m:
    print(end)
else:
    result = 0
    while (start <= end):
        total = 0
        # 상한가
        mid = (start + end) // 2

        for x in array:
            # 요청 예산이 상한가보다 크다면 상한가로 계산
            if x > mid:
                total += mid
            else:  # 요청 예산이 상한가랑 같거나 작다면 요청 예산으로 계산
                total += x

        if total <= m:
            result = mid
            start = mid + 1

        else:
            end = mid - 1

    print(result)
