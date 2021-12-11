a, b, c = map(int, input().split())

d = c if ((a if(a < b) else b) > c) else (a if(a < b) else b)
print(d)
