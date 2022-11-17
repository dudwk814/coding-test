def solution(lottos, win_nums):
    answer = []
    zero = lottos.count(0)
    count = 0
    for i in win_nums:
        if i == 0:
            continue

        if i in lottos:
            count += 1
    min_vlaue = count
    count += zero

    if count == 6:
        answer.append(1)
    elif count == 5:
        answer.append(2)
    elif count == 4:
        answer.append(3)
    elif count == 3:
        answer.append(4)
    elif count == 2:
        answer.append(5)
    else:
        answer.append(6)

    if min_vlaue == 6:
        answer.append(1)
    elif min_vlaue == 5:
        answer.append(2)
    elif min_vlaue == 4:
        answer.append(3)
    elif min_vlaue == 3:
        answer.append(4)
    elif min_vlaue == 2:
        answer.append(5)
    else:
        answer.append(6)

    return answer
