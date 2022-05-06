input_data = input()

result = 0
while True:
    if int(input_data) >= 10:
        temp = 0
        for i in input_data:
            temp += int(i)

        result += 1
        input_data = str(temp)
    else:
        if int(input_data) % 3 == 0:
            print(result)
            print("YES")
            break
        else:
            print(result)
            print("NO")
            break
