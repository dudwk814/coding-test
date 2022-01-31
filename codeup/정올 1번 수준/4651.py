from itertools import count


for i in range(3):
    input_data = list(map(int, input().split()))

    if input_data.count(0) == 1:
        print('A')
    elif input_data.count(0) == 2:
        print('B')
    elif input_data.count(0) == 3:
        print('C')
    elif input_data.count(0) == 4:
        print('D')
    else:
        print('E')
