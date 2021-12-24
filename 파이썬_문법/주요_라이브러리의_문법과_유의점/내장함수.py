# 내장 함수
# 내장 함수는 별도의 import 명령어 없이  바로 사용할 수 있다.
result = sum([1, 2, 3, 4, 5])  # 파라미터의 총 합을 반환
print(result)

result = min([7, 3, 5, 2])  # 가장 작은 값을 반환
print(result)

result = max([7, 3, 5, 2])  # 가장 큰 값을 반환
print(result)

result = eval("(3+5) * 7")  # 수식이 문자열 형태로 들어오면 해당 수식을 계산하여 반환
print(result)


result = sorted([9, 1, 8, 5, 4])
print(result)

result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)

result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)],
                key=lambda x: x[1], reverse=True)
print(result)

data = [9, 1, 8, 5, 4]
data.sort()
print(*data)
