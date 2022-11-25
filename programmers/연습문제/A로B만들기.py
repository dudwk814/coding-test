def solution(before, after):
    answer = 1

    for i in range(len(after)):
        a_count = after.count(after[i])
        b_count = before.count(after[i])

        if a_count != b_count:
            answer = 0
            break
    return answer


solution("allpe", "apple")
