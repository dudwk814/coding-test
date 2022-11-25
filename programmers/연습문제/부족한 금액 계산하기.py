def solution(price, money, count):
    answer = -1

    charge = 0

    for i in range(1, count + 1):
        charge += price * i

    if money >= charge:
        answer = 0
    else:
        answer = charge - money
    return answer


solution(3, 20, 4)
