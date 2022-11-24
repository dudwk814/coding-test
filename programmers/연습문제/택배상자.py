from collections import deque


def solution(order):
    answer = 0
    array = [i for i in range(max(order), 0, -1)]

    for i in range(len(order)):
        print(array)
        if order[i] == array[0]:
            answer += 1
            array.popleft()

    return answer


print(solution([2, 1, 6, 7, 5, 8, 4, 9, 3, 10]))
