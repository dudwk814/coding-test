# a 부터 b까지 오름차순으로 정렬
# ex) a = 5, b = 10일 경우 5 6 7 8 9 10 출력
a, b = map(int, input().split())

if a < b:
    for i in range(a, b + 1):
        print(i, end=' ')

if a == b:
    print(a)

if a > b:
    for i in range(b, a + 1):
        print(i, end=' ')
