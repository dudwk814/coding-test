n = int(input())

people = []

for i in range(n):
    name, day, month, year = input().split()
    day, month, year = int(day), int(month), int(year)

    people.append([name, day, month, year])

people.sort(key=lambda x: (x[3], x[2], x[1]))

print(people[n - 1][0])
print(people[0][0])
