# n 이 입력되면 k를 빼서 제곱수를 만들 수 있는 k를 구하고, 그 제곱수에 루트를 씌운 수(제곱근) t를 구하여라.
# k는 여러가지 경우의 수 중 가장 작은 수

import math

n = int(input())

k = 0   # n에서 k를 뺐을때 n - k가 제곱수가 될 수 있는 정수 중 가작 작은 수
t = 0   # n - k가 제곱수일때 n-k를 만족하는 제곱근 t * t = n - k
square_number = 0  # 제곱수

for i in range(1, n + 1):
    square_number = n - i
    # math.sqrt() = 제곱근을 구해주는 함수, is_integer() = float 타입의 수가 정수라면 true
    if math.sqrt(square_number).is_integer() == True:

        k = i
        t = int(math.sqrt(square_number))
        break
print(k, t, end=' ')
