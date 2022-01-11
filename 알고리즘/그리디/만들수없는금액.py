n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 1
count = 0

for i in data:
    
    if result in data:
        result += 1
        count += i  
        continue
    elif result == count:
        result += 1
        count += i  
        continue
    else:
        break
      

print(result)