def solution(s):
    answer = ''
    upper = []
    lower = []

    for i in range(len(s) - 1, -1, -1):
        if s[i].isupper():
            upper.append(s[i])
        else:
            lower.append(s[i])
    lower.sort(reverse=True)
    upper.sort(reverse=True)

    for i in lower:
        answer += i
    for i in upper:
        answer += i

    return answer
