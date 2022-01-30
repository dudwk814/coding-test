n = int(input())

if n <= 500:
    print(int(n * 0.7))
elif n <= 1500:
    print(int(350 + ((n - 500) * 0.4)))
elif n <= 4500:
    print(int(750 + ((n - 1500) * 0.15)))
elif n <= 10000:
    print(int(1200 + ((n - 4500) * 0.05)))
else:
    print(int(1475 + ((n - 10000) * 0.02)))    
