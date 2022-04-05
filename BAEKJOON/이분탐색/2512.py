import sys
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

start = 0
end = max(array)
result = 0

while (start <= end):
    mid = (start + end) // 2
    total = 0

    for x in array:
        if x > mid:
            x = mid
        total += x

    if total <= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
