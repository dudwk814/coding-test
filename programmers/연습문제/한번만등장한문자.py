def solution(s):
    answer = ''
    array = []
    for i in s:
        if s.count(i) == 1:
            array.append(i)
    array.sort()

    for i in array:
        answer += i
    return answer
