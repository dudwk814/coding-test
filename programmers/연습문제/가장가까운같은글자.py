def solution(s):
    answer = []

    for i in range(len(s)):
        array = s[:i]

        if array.count(s[i]) >= 1:
            idx = 0
            for j in range(i):
                if s[j] == s[i]:
                    idx = max(idx, j)
            answer.append(i - j)
        else:
            answer.append(-1)

    return answer
