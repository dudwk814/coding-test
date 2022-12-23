n = int(input())

for i in range(n):
    score = list(map(int, input().split()))
    score.remove(score[0])
    max_score = max(score)
    min_score = min(score)
    gap = 0

    score.sort(reverse=True)

    for j in range(len(score) - 1):
        gap = max(gap, score[j] - score[j + 1])
    print("Class", i + 1)
    print(f"Max {max_score}, Min {min_score}, Largest gap {gap}")
