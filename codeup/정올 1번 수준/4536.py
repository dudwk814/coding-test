from itertools import count


d = []
count = [0] * 1000
for i in range(10):
    input_data = int(input())
    d.append(input_data)
    count[input_data] += 1


print(int(sum(d) / 10))

for i in range(len(count)):
    if max(count) == count[i]:
        print(i)
        break
