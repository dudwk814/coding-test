t = int(input())

for i in range(t):
    input_data = list(map(int, input().split()))

    input_data.sort(reverse=True)

    print(input_data[2])
