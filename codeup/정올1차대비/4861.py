n, k = map(int, input().split())  # 학생의 수, 한 방에 들어갈 수 있는 최대 인원 수
count = 0  # 총 방의 수
student = [[0] * 2 for _ in range(7)]  # 1 ~ 6학년 까지의 정보 테이블

for i in range(n):
    s, y = map(int, input().split())

    if s == 0:
        student[y][0] += 1
    else:
        student[y][1] += 1

for i in range(1, 7):
    for j in range(2):
        count += student[i][j] // k

        if student[i][j] % k >= 1:
            count += 1
print(count)
