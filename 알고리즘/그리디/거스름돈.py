# n = 1260  # 총 거스름 돈
# count = 0  # 거스름돈의 동전 개수

# # 큰 단위의 화폐부터 차례대로 확인
# coin_types = [500, 100, 50, 10]

# for coin in coin_types:
#     count += n // coin  # 총 거스름돈을 coin으로 나눈 몫을 count에 더함 ex) 1260 // 500 = 2
#     n %= coin  # n을 coin으로 나눈 나머지를 n에 다시 저장

# print(count)

n = int(input())
count = 0

coin_types = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)
