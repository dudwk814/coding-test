s = input()
start = 0
end = len(s)

stat = True

while start < end:

    if s[start] == "p" and end - start > 1:
        if s[start + 1] == "i":
            start += 2
            continue
        else:
            stat = False
            break

    elif s[start] == "k" and end - start > 1:
        if s[start + 1] == "a":
            start += 2
            continue
        else:
            stat = False
            break
    elif s[start] == "c" and end - start > 2:
        if s[start + 1] == "h" and s[start + 2] == "u":
            start += 3
            continue
        else:
            stat = False
            break
    else:
        stat = False
        break

if stat:
    print("YES")
else:
    print("NO")
