n, m = map(int, input().split())
input_data = list(map(int, input().split()))
count = 0

for i in range(len(input_data)):
    for j in range(i + 1, len(input_data)):
        if input_data[i] != input_data[j]:
            count += 1

print(count)