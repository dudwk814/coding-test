import math


def solution(n, m):
    answer = []

    answer.append(math.gcd(n, m))
    answer.append(math.lcm(n, m))
    return answer


solution(3, 12)
