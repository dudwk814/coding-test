n = int(input())  # 토핑 종류의 수
a, b = map(int, input().split())  # a = 도우 가격, b = 토핑 가격
c = int(input())  # 도우의 칼로리

data = []  # 토핑 리스트
s = 0
for i in range(n):  # 토핑 종류 만큼 칼로리 입력
    t = int(input())
    data.append(t)
data.sort()    
print(*data)
