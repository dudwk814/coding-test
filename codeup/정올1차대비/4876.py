n = int(input())

for i in range(n):
    scoreA = [0] * 5
    scoreB = [0] * 5

    a_input = list(map(int, input().split()))
    b_input = list(map(int, input().split()))

    for j in range(1, len(a_input)):
        scoreA[a_input[j]] += 1

    for j in range(1, len(b_input)):
        scoreB[b_input[j]] += 1

    for k in range(4, 0, -1):
        if scoreA[k] > scoreB[k]:
            print('A')
            break
        elif scoreA[k] < scoreB[k]:
            print('B')
            break

        if k == 1:
            if scoreA[k] == scoreB[k]:
                print('D')
                break
