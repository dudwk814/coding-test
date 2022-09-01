s = input()

array = [0] * 26

for i in s:

    idx = ord(i) - ord('a')

    array[idx] += 1

print(* array)    