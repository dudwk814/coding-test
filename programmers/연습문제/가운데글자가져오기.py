def solution(s):
    answer = ''

    len_s = len(s)
    mid = len_s // 2

    if len_s % 2 == 0:
        answer = s[mid - 1] + s[mid]
    else:
        answer = s[mid]
    return answer


print(solution("qwer"))
