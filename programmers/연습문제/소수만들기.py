from itertools import combinations


def solution(nums):
    answer = 0

    array = list(combinations(nums, 3))

    for i in array:
        sum_value = sum(i)
        decimal = True
        for j in range(2, sum_value):
            if sum_value % j == 0:
                decimal = False

            if not decimal:
                break

        if decimal:
            answer += 1

    print(answer)

    return answer


solution([1, 2, 7, 6, 4])
