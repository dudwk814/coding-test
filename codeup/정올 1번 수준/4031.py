input_data = list(map(int, input().split()))

even = [0] * 7
odd = [0] * 7

for i in input_data:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

evenMax = max(even)
oddMax = max(odd)
print(evenMax + oddMax)
