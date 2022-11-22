def solution(num):
    answer = 0

    if num == 1:
        return answer

    for i in range(501):
        if i == 500:
            answer = -1
            return answer

        if num == 1:
            return answer
        if num % 2 == 0:
            num /= 2
            answer += 1
        elif num % 2 != 0:
            num = num * 3 + 1
            answer += 1
    return answer


print(solution(626331))
