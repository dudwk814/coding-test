# 리스트 컴프리헨션: 리스트를 초기화하는 방법 중 하나
# 대괄호([])안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화

# 0부터 19까지의 수 중에서 홀수만 포함한 리스트 생성
array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [i * i for i in range(0, 10)]
print(array)

# n * m 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(*array)

# 19 * 19 바둑판 형태의 2차원 리스트 초기화
array = [[0] * 19 for _ in range(19)]
print(array)
