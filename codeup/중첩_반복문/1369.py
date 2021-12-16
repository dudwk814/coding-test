# 빗금 친 사각형 출력하기

n, k = map(int, input().split())

for i in range(n):
    for j in range(1, n + 1):
        # i가 처음이거나 마지막인 경우 *을 n개 만큼 찍고 break (위 아래 *)
        if i == 0 or i == n - 1:
            print('*'*n, end='')
            break
        if j == 1 or j == n:    # j가 처음이거나 마지막인 경우 *을 찍음 (사이드 테두리 *)
            print('*', end='')
        elif (j + i) % k == 0:  # 빗금 방향이 왼쪽 아래를 향하기 때문에  j + i를 k로 나눈 나머지가 0 (k의 배수)인 경우 *을 찍음 (빗금)
            print('*', end='')
        else:  # 나머지 공간을 공백으로 채움
            print(' ', end='')
    print()
