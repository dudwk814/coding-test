n = int(input())
ans = 0
word = input()

for i in range(n):
    value = int(word[i])
    ans += value

print(ans)
