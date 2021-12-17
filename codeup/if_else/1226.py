# 이번 주 로또

prize = list(map(int, input().split()))
no = list(map(int, input().split()))
d = 0
bonus = False

for i in range(len(no)):
    for j in range(len(prize)):

        if no[i] == prize[len(prize) - 1]:  # 지혜의 번호가 보너스 번호와 맞다면 bonus를 True로 변경
            bonus = True
            break

        if no[i] == prize[j]:
            d += 1
            continue


if d == 6:
    print(1)
elif d == 5 and bonus:
    print(2)
elif d == 5:
    print(3)
elif d == 4:
    print(4)
elif d == 3:
    print(5)
else:
    print(0)
