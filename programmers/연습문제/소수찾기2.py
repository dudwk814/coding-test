from itertools import permutations


def solution(numbers):
    answer = 0
    com = []
    for i in range(1, len(numbers) + 1):
        array = list(permutations(numbers, i))
        com.extend(array)

    for i in range(len(com)):
        num = ''
        for j in com[i]:
            num += j
        com[i] = int(num)

    com = list(set(com))

    for value in com:
        if value < 2:
            continue

        prime = False
        for i in range(2, value):
            if value % i == 0:
                prime = True
                break

        if not prime:
            answer += 1
    print(answer)
    return answer


solution("011")
