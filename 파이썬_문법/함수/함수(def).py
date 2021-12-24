# 함수의 형태 (더하기 기능을 제공하는 함수)
def add(a, b):
    return a + b


print(add(3, 7))


def add(a, b):
    print(a + b)


add(3, 7)

add(b=7, a=3)

a = 0


def func():
    global a
    a += 1


for i in range(10):
    func()
print(a)

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))
