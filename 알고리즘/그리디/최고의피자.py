n = int(input())  # 토핑 종류의 수
a, b = map(int, input().split())  # a = 도우 가격, b = 토핑 가격
c = int(input())  # 도우의 칼로리

data = []  # 토핑 리스트
for i in range(n):  # 토핑 종류 만큼 칼로리 입력
    t = int(input())
    data.append(t)
data.sort(reverse=True)

price = a
cal = c
r = 0
best_pizza = []
for topping in data:
    price += b
    cal += topping
    r = int(cal / price)
    best_pizza.append(r)

best_pizza.sort(reverse=True)
print(best_pizza[0])
