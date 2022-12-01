def solution(a, b):
    answer = ''

    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    a = sum(month[:a])
    a += b

    count = 0
    for i in range(a):
        if count == 7:
            count = 0

        if count == 0:
            answer = "FRI"
            count += 1
        elif count == 1:
            answer = "SAT"
            count += 1
        elif count == 2:
            answer = "SUN"
            count += 1
        elif count == 3:
            answer = "MON"
            count += 1
        elif count == 4:
            answer = "TUE"
            count += 1
        elif count == 5:
            answer = "WED"
            count += 1
        elif count == 6:
            answer = "THU"
            count += 1

    return answer


solution(5, 24)
