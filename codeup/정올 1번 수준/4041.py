n = input()
d = []

for i in range(len(n) - 1, -1, -1):
    d.append(int(n[i]))
print(int(n[::-1]))
print(sum(d))
