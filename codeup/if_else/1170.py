# 당신의 학번은? 1
no = list(map(int, input().split()))

for i in range(len(no)):

    if i == len(no) - 1:
        if no[i] < 10:
            print(0, no[i], sep='', end='')
            break

    print(no[i], end='')
