def solution(phone_number):
    answer = ''

    len_num = len(phone_number)

    for i in range(len_num):
        if len_num - i > 4:
            answer += "*"
        else:
            answer += phone_number[i]
    return answer
