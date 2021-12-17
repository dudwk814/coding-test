# 비만도 측정 2

h, w = map(float, input().split())

if h < 150:
    avg = h - 100
elif h >= 150 and h < 160:
    avg = (h - 150) / 2 + 50
else:
    avg = (h - 100) * 0.9

bmi = (w - avg) * 100 / avg

if bmi <= 10:
    print('정상')
elif bmi <= 20:
    print('과체중')
else:
    print('비만')
