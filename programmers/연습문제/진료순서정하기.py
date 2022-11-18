def solution(emergency):
    answer = []

    for i in range(len(emergency)):
        emergency[i] = (emergency[i], i)
    emergency.sort(key=lambda x: -x[0])

    for i in range(len(emergency)):
        emergency[i] = (emergency[i][0], emergency[i][1], i + 1)

    emergency.sort(key=lambda x: x[1])

    for i in emergency:
        answer.append(i[2])

    return answer


emergency = list(map(int, input().split()))

print(solution(emergency))
