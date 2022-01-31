n = int(input())
max_value = 0
double = []
for i in range(n):
    input_data = list(map(int, input().split()))
    double.clear()
    for j in input_data:
        if input_data.count(j) == 4:
            max_value = max(max_value, 50000 + (j * 5000))
            break
        elif input_data.count(j) == 3:
            max_value = max(max_value, 10000 + (j * 1000))
            break
        elif input_data.count(j) == 2:
            for k in input_data:
                if j != k and input_data.count(k) == 2:
                    max_value = max(max_value, 2000 + (j * 500) + (k * 500))
                    break
                elif j == k:
                    continue
                else:
                    max_value = max(max_value, 1000 + (j * 100))
                    break
            break
        else:
            max_value = max(max_value, max(input_data) * 100)

print(max_value)