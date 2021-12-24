# in 연산자 : 리스트, 튜플등과 같이 여러 개의 데이터를 담는 자료형에서 어떤 값이 존재하면 True
# not in 연산자: 여러 개의 데이터를 갖는 자료형 안에 어떤 데이터가 존재하지 않는다면 True

# pass : 조건문의 값이 참(True)이여도, 아무것도 처리하고 싶지 않을 때 사용 가능

score = 85

if score >= 80:
    pass
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')

# 조건문 안에 실행코드가 한 줄이라면 줄 바꿈을 하지 않아도 됨
score = 85

if score >= 80:
    result = "Sccess"
else:
    result = "Fail"

print(result)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)

# 파이썬은 조건문 안에서 수학의 부등식을 그대로 사용 가능 ex) if 0 < x < 20: x가 0보다 크고 20보다 작으면 True
