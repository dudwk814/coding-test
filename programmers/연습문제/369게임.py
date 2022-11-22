def solution(order):
    order_str = str(order)
    answer = 0
    for i in order_str:
        if i == "3":
            answer += 1
        elif i == "6":
            answer += 1
        elif i == "9":
            answer += 1

    return answer
