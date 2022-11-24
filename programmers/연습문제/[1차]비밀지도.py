def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        arr1_value = str(bin(arr1[i]))[2:]
        arr2_value = str(bin(arr2[i]))[2:]
        if len(arr1_value) < n:
            sub = n - len(arr1_value)
            arr1_value = '0' * sub + arr1_value
        if len(arr2_value) < n:
            sub = n - len(arr2_value)
            arr2_value = '0' * sub + arr2_value

        array = ""
        for j in range(n):

            if arr1_value[j] == "1" or arr2_value[j] == "1":
                array += "#"
            else:
                array += " "
        answer.append(array)
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
