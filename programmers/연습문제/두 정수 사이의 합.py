def solution(a, b):
    max_value = max(a, b)
    min_value = min(a, b)
    array = [x for x in range(min_value, max_value + 1)]

    print(array)
    answer = sum(array)
    return answer
