# 이 사람이 투자한 돈의 액수와, 그 주식의 하루간의 변동을 퍼센트로 알 때,
# 이 사람의 순수익과 이득/손해 판단을 출력
a = int(input())  # 투자한 액수
b = int(input())  # 투자 일
result = a

d = list(map(int, input().split()))  # 투자 일 별 이득 손해 퍼센트

for i in range(0, b): # 투자 일수 만큼 루프를 돌려 손익을 계산
    profit = (result / 100) * (+(d[i]))  # profit = 하루 손익
    result = result + profit  # result = 투자액 + 하루 손익

result = result - a # result = 투자 액 - 총 손익 

print(format((result), ".0f")) # 손익 출력 양수, 혹은 음수

if result > 0:  # 총 손익이 양수면 good, 0이면 same, 음수면 bad
    print("good")
elif result == 0:
    print("same")
else:
    print("bad")        
