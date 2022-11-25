from itertools import product


def solution(word):
    answer = 0
    array = ['A', 'E', 'I', 'O', 'U']
    array2 = []
    for i in range(1, 6):

        array2.extend(list(product(array, repeat=i)))

    for i in range(len(array2)):
        value = ''
        for j in array2[i]:
            value += j
        array2[i] = value

    array2 = list(set(array2))
    array2.sort()

    idx = array2.index(word) + 1
    print(idx)
    return idx


solution("AAAE")
