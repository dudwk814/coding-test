def solution(age):
    answer = ''
    age = str(age)

    for i in age:
        i = chr(ord("a") + int(i))
        answer += i
    return answer
