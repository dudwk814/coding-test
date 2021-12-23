# 실수형은 소수점 아래의 데이터를 포함한 수 자료형
# 소수부가 0이거나, 정수부가 0인 소수는 0을 생략할 수 있다.

# 양의 실수
a = 157.93
print(a)

# 음의 실수
a = -1837.2
print(a)

# 소수부가 0일 때 0을 생략
a = 5.
print(a)

# 정수부가 0일 때 0을 생략
a = -.7
print(a)

# 10억의 지수 표현 방식
a = 1e9
print(a)

# 752.5
a = 75.25e1
print(a)

# 3.954
a = 3954e-3
print(a)

# round()함수는 첫 번째 파라미터를 두 번째 파라미터 자리까지 표현, 두 번째 파라미터 뒷 자리에서 반올림
a = 0.3 + 0.6
print(round(a, 4))

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)
