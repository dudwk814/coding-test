button = [300, 60, 10]
count = [0] * 3
t = int(input())

if t % button[2] == 0:
    for i in range(len(button)):
        if t // button[i] >= 1:
            count[i] += t // button[i]
            t %= button[i]
        print(count[i], end=' ')
else:
    print(-1)
