home = list(map(int, input().split()))
away = list(map(int, input().split()))

score = False

for i in range(9):
    hs = sum(home[:i + 1])
    aws = sum(away[:i])

    if hs > aws:
        score = True
        break

if score:
    print("Yes")
else:
    print("No")
