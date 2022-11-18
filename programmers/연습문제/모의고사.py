def solution(answers):

    answer = []
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    list_count_1 = int(10000 / len(student_1))
    list_count_2 = int(10000 / len(student_2))
    list_count_3 = int(10000 / len(student_3))

    student_1 = student_1 * list_count_1
    student_2 = student_2 * list_count_2
    student_3 = student_3 * list_count_3

    count1 = 0
    count2 = 0
    count3 = 0

    for i in range(len(answers)):
        if answers[i] == student_1[i]:
            count1 += 1
        if answers[i] == student_2[i]:
            count2 += 1
        if answers[i] == student_3[i]:
            count3 += 1

    max_count = max(count1, count2, count3)

    if count1 == max_count:
        answer.append(1)
    if count2 == max_count:
        answer.append(2)
    if count3 == max_count:
        answer.append(3)

    return answer


solution([1, 2, 3, 4, 5])
