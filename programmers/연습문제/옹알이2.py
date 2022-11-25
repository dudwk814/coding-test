from itertools import permutations


def solution(babbling):
    array = []
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for i in range(1, 5):
        word = list(permutations(words, i))
        array.extend(word)
    for i in range(len(array)):
        word = ""
        for j in array[i]:
            word += j
        array[i] = word

    for word in babbling:
        if word in array:
            answer += 1

    return answer


solution(["aya", "yee", "u", "maa"])
