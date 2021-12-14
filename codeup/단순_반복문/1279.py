# 두 자연수 a, b 사이의 구간에 대해서 홀수는 더하고 짝수는 뺀다음의 합을 출력

a, b = map(int, input().split())
result = 0

if a == b:  # a와 b가 같다면
    if a % 2 != 0:  # 홀수라면 더하기
        a += a
    else:   # 짝수라면 빼기
        a -= a
    print(a)
elif a < b:
    for i in range(a, b + 1):
        if i % 2 != 0:  # 홀수라면 더하기
            result += i
        else:  # 짝수라면 빼기
            result -= i

print(result)
