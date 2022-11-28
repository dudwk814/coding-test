from itertools import permutations


def solution(X, Y):
    answer = []
    s = []
    array = []

    for i in range(10):
        x_count = str(X).count(str(i))
        y_count = str(Y).count(str(i))

        min_count = min(x_count, y_count)
        if x_count == y_count:

            s.extend([str(i) for _ in range(x_count)])
        else:
            s.extend([str(i) for _ in range(min_count)])

    s_len = len(s)

    
    num = list(set(list(permutations(s, 9))))

    array.extend(num)

    for i in range(len(array)):
        number = ''

        number = ''.join(array[i])

        if number.count("0") == len(number):
            answer.append('0')
        else:
            answer.append(number)
    answer = list(set(answer))

    if len(answer) == 0:
        return "-1"

    return max(answer)


solution("5525", "1255")
