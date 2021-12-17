# 비만도 측정 1

height, weight = map(float, input().split())
avg = (height - 100) * 0.9
bmi = (weight - avg) * 100 / avg

if bmi <= 10:
    print('정상')
elif bmi <= 20:
    print('과체중')
else:
    print('비만')
