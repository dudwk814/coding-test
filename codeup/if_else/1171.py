# 당신의 학번은? 2

no = list(map(int, input().split()))

for i in range(len(no)):

    if i == 1:
        if no[i] < 10:
            print(0, no[i], sep='', end='')
            continue
    if i == 2:
        if no[i] < 10:
            print(0, 0, no[i], sep='', end='')
            break
        elif no[i] < 100:
            print(0, no[i], sep='', end='')
            break

    print(no[i], end='')
