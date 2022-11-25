def solution(s):
    answer = []
    count = 0
    removed_zero = 0

    while s != "1":
        removed_zero += s.count("0")
        s = s.replace("0", '')
        s_len = len(s)
        s = bin(s_len)[2:]
        count += 1
    answer = [count, removed_zero]
    return answer


print(solution("110010101001"))
