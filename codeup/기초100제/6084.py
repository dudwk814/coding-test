h, b, c, s = map(int, input().split())

# 소리의 용량을 MB단위로 표현하기 위해 8/1024/1024로 나눠야함
result = h * b * c * s / 8 / 1024 / 1024

print(format(result, ".1f"), "MB")
