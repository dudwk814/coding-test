def solution(hp):
    answer = 0
    ants = [5, 3, 1]

    for i in ants:
        if hp >= i:
            answer += hp // i
            hp %= i
    return answer


hp = int(input())
print(solution(hp))
