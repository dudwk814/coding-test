n = int(input())

input_data = list(map(int, input().split()))

score = [x for x in input_data]

max_value = max(score)
min_value = min(score)
print(max_value - min_value)
