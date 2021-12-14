# 자연수 a, b 사이의 구간에 대해서 홀수는 더하고 짝수는 빼는 식을 보여준 후 결과를 출력
a, b = map(int, input().split())
result = 0
calculation = ""

if a == b:  # a와 b가 같다면
    if a % 2 != 0:  # 홀수라면 더하기 식과 결과 출력
        result += a
        print("%d" % a + "=" + "%d" % result)
    else:  # 짝수라면 빼기 식과 결과 출력
        result -= a
        print("-" + "%d" % a + "=" + "%d" % result)
elif a < b:  # a가 b보다 작으면
    for i in range(a, b + 1):

        if i % 2 != 0 and i == a:
            calculation = "%d" % i
            result += i

        elif i % 2 != 0 and i != a:
            calculation = calculation + "+" + "%d" % i
            result += i
        else:
            calculation = calculation + "-" + "%d" % i
            result -= i
    print(calculation + "=" + "%d" % result)
