def solution(my_string):
    array = list(dict.fromkeys(my_string))
    answer = ''
    for i in array:
        answer += i
    return answer
