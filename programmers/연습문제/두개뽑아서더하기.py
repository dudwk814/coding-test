from itertools import combinations


def solution(numbers):
    answer = []
    array = list(combinations(numbers, 2))
    for i in range(len(array)):
        value = array[i][0] + array[i][1]
        answer.append(value)

    answer = list(set(answer))
    answer.sort()
    return answer


solution([2, 1, 3, 4, 1])
