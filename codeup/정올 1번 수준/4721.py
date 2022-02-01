n = int(input())
max_value = 0
student1 = [0] * 5
student2 = [0] * 5
student3 = [0] * 5
result = []

for i in range(n):
    a, b, c = map(int, input().split())
    student1[a] += 1
    student2[b] += 1
    student3[c] += 1

for i in range(3):
    for j in range(1, 4):
        if i == 0:
            student1[4] += student1[j] * j
        elif i == 1:
            student2[4] += student2[j] * j
        else:
            student3[4] += student3[j] * j

max_value = max(student1[4], student2[4], student3[4])

for i in range(3):
    if i == 0:
        if student1[4] == max_value:
            result.append((1, student1[4], student1[3], student1[2]))
    elif i == 1:
        if student2[4] == max_value:
            result.append((2, student2[4], student2[3], student2[2]))
    else:
        if student3[4] == max_value:
            result.append((3, student3[4], student3[3], student3[2]))


result.sort(key=lambda student: (-student[2], -student[3]))

max3 = result[0][2]
max2 = result[0][3]
equal3 = True
eqaul2 = True

if len(result) >= 2:
    for i in range(1, len(result)):
        if max3 != result[i][2]:
            print(result[0][0], result[0][1])
            equal3 = False
            break
    if equal3:
        for i in range(1, len(result)):
            if max2 != result[i][3]:
                print(result[0][0], result[0][1])
                eqaul2 = False
                break
    if equal3 and eqaul2:
        print(0, max_value)
else:
    print(result[0][0], result[0][1])
