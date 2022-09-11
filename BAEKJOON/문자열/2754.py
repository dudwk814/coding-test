c = input()
score = 0.0

if 'A' in c:
    score += 4.0
elif 'B' in c:
    score += 3.0
elif 'C' in c:
    score += 2.0
elif 'D' in c:
    score += 1.0

if '+' in c:
    score += 0.3
elif '-' in c:
    score -= 0.3

print(score)
