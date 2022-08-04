import sys
n = int(sys.stdin.readline())

s = []

for i in range(n):
    s.append(int(sys.stdin.readline()))
answer = 0

if len(s) > 1:
    while True:
        max_value = max(s[1:])
        if s[0] > max(s[1:]):
            break
        else:
            if s[0] == max_value:
                answer += 1
                s[0] += 1
                max_value_index = s.index(max_value)
                s[max_value_index] -= 1
            else:
                max_value_index = s.index(max(s))
                answer += 1
                s[0] += 1
                s[max_value_index] -= 1
print(answer)
