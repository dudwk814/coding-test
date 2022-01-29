d = 0
for i in range(5):
    start, end = map(float, input().split())

    if end - start >= 5.0:
        d += 4.0
        continue
    if end - start > 1.0:
        d += end - start - 1.0

if d <= 5.0:
    d *= 1.05
elif d >= 15.0:
    d *= 0.95

print(int((d / 0.5) * 5000))
