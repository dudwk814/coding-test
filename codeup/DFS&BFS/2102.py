n = input()
multiple = n

while True:

    notZeroOrOne = False

    # multiple의 첫 값이 1인 경우 나머지 값이 0 혹은 1인지 조사하고 0 혹은 1이라면 n의 배수인지 조사
    if multiple[0] == '1':
        for i in range(1, len(multiple)):

            for j in range(2, 10):
                if int(multiple[i]) == j:
                    notZeroOrOne = True
                    break
            if notZeroOrOne == True:
                break
    else:  # 첫 값이 1이 아닌 경우 다음 루프로 가기위해 notZeroOrOne 값을 True로 변경
        notZeroOrOne = True

    if notZeroOrOne == True:  # 나머지 값이 0 혹은 1이 아닌 경우 continue
        multiple = str(int(multiple) + int(n))  # 첫 값이 1이지만 나머지 값이
        continue

    if int(multiple) > 2 ** 64:
        print(0)
        break

    # 첫 값이 1 나머지 값이 0 혹은 1이면서 n의 배수인 경우 출력하고 종료
    print(multiple)
    break
