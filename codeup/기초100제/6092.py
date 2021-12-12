n = int(input())  # 총 부른 횟수

a = input().split()  # 부른 출석부의 리스트

for i in range(n):  # 0 ~ n -1 까지 루프
    a[i] = int(a[i])  # a[i]의 값을 정수화하여 다시 a[i]에 저장

d = []  # 빈 리스트를 생성하여 출석부 번호를 초기화

for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]] += 1

for i in range(1, 24):
    print(d[i], end=' ')
