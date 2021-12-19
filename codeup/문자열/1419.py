# love 2
s = input().split()
result = 0
for i in range(len(s)):
    if s[i].count("love"):
        result += s[i].count("love")

print(result)
