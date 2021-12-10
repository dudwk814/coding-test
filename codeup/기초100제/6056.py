a, b = map(int, input().split())

c, d = bool(a), bool(b)
print((c and (not d)) or (not c and (d)))

# 2개의 boolean 값을 받아 출력하는데 두 값이 true면 false를 출력하고 둘 중 하나라도 false면 true를 출력
