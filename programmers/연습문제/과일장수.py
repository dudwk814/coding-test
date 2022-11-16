def solution(k, m, score):
    answer = 0
    scoreLen = len(score)

    if scoreLen < m:
        return answer

    score.sort(reverse=True)

    array = []
    for i in range(scoreLen):

        array.append(score[i])

        if len(array) == m:
            answer += min(array) * m
            array = []

    return answer
