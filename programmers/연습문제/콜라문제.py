def solution(a, b, n):
    answer = 0
    count = 0

    while True:
        if n // a > 0:
            answer += (n // a) * b
            count = n % a
            n = (n // a) + count
        else:
            break
    return answer


solution(3, 1, 20)
