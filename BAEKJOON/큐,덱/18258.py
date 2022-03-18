from collections import deque
import sys
d = list()
q = deque(d)

n = int(input())

for i in range(n):
    input_data = sys.stdin.readline()

    if input_data[0] == 'p':
        if input_data[1] == 'u':  # 명령어가 push인 경우
            push_data = input_data.split(' ')
            q.append(int(push_data[1]))
        else:  # 명령어가 pop인 경우
            if len(q) == 0:
                print(-1)
            else:
                pop_data = q.popleft()
                print(pop_data)
    elif input_data[0] == 's':
        print(len(q))
    elif input_data[0] == 'e':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif input_data[0] == 'f':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif input_data[0] == 'b':
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q) - 1])
