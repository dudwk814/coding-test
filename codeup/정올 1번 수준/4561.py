odd = []

for i in range(7):
    input_data = int(input())

    if input_data % 2 != 0:
        odd.append(input_data)

if len(odd) == 0:
    print(-1)
else:
    print(sum(odd))
    print(min(odd))
