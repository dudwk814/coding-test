a, b = input().split('-')
year = a[:2]
if int(year) <= 9 and (b[0] == '3' or b[0] == '4'):
    year = int(year) + 2000
else:
    year = int(year) + 1900
sex = b[0]
if sex == '1' or sex == '3':
    sex = 'M'
else:
    sex = 'F'
print(year, a[2:4], a[4:6], sep='/', end=' ')
print(sex)
