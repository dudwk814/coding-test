n = int(input())
member = []

for i in range(n):
    age, name = input().split()
    age = int(age)

    member.append((age, name, i))

member.sort(key=lambda x: (x[0], x[2]))

for i in member:
    print(i[0], i[1])
