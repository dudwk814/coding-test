def solution(k, score):
    answer = []
    array = []
    for i in range(len(score)):
        array.append(score[i])
        array.sort()

        if len(array) > k:
            answer.append(array[1])
            array.remove(array[0])
        else:
            answer.append(array[0])
    print(answer)
    return answer


solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])
