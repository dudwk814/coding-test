def solution(arr):
    answer = arr
    answer.remove(min(answer))

    if len(answer) == 0:
        return [-1]
    return answer
