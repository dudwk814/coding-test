# 스택 : 선입후출의 구조를 가진 자료구조

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)  # 최하단 원소부터 출력
print(stack[::-1])
