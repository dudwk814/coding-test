# 큰수 - 작은수
a, b = map(int, input().split())

big = a if a > b else b
small = a if a < b else b

print(big - small)
