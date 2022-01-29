trigger = False
result = 0
input_data = list(map(int, input().split()))

for i in input_data:
    if i % 2 != 0:
        trigger = True
        result += i

if not trigger:
    print(-1)
else:
    print(result)
