from itertools import count
import sys

t = int(input())

for i in range(t):
    n = int(input())

    s = []

    for j in range(n):
        score = int(sys.stdin.readline().rstrip())
        s.append(score)

    sum_score = sum(s)

    idx = s.index(max(s)) + 1

    if s.count(max(s)) >= 2:
        print("no winner")
    elif max(s) > sum_score / 2:

        print("majority winner", idx)
    elif max(s) <= sum_score / 2:

        print("minority winner", idx)
