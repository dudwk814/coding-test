data = list(map(int, input()))
left_side = 0
right_side = 0

for i in range((len(data) // 2)):
    left_side += data[i]

for i in range(len(data) // 2, len(data)):
    right_side += data[i]

if left_side == right_side:
    print('LUCKY')
else:
    print('READY')
