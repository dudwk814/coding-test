n = int(input())
word = []

for i in range(n):
    s = input()
    word.append((s, len(s)))
word = list(set(word))
word.sort(key=lambda x: (x[1], x[0]))

for i in word:
    print(i[0])
