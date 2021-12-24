# 파이썬의 반복문은 for문과 while문이 있다.

# while문
# while문은 조건이 참일 때 한해서, 반복적으로 코드가 수행됨
i = 1
result = 0

# i가 9보다 작거나 같을 때 까지 아래 코드를 반복적으로 수행
while i <= 9:
    result += i
    i += 1

print(result)

i = 1
result = 0

while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1
print(result)

# for문
result = 0
for i in range(1, 10):
    result += i

print(result)

score = [90, 85, 77, 65, 97]

for i in range(5):
    if score[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

score = [90, 85, 77, 65, 97]
cheating_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_list:
        continue
    if score[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")


# 2중 for문 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "x", j, "=", (i * j), end=' ')
    print()
