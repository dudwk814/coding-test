s = input()
array = [-1] * 26

for i in range(len(s)):
    w = s[i]

    idx = ord(w) - ord('a')

    if array[idx] == -1:
        array[idx] = i

print(*array)
