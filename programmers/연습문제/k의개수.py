def solution(i, j, k):
    answer = 0

    for a in range(i, j + 1):
        a = str(a)

        for w in a:
            if str(k) == w:
                answer += 1
    return answer


solution(1, 13, 1)
