s = input()

array = [0] * 26

for w in s:

    ord_w = ord(w)

    if ord_w < 97:
        idx = ord_w - 65

        array[idx] += 1
    else:
        idx = ord_w - 97

        array[idx] += 1


max_count = max(array)

if array.count(max_count) > 1:
    print('?')
else:
    idx = array.index(max_count) + 65

    print(chr(idx))
