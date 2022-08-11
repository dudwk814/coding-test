
t = int(input())

for i in range(t):

    s = [[0] for i in range(ord('Z') - ord('A') + 1)]
    word = input()

    ok = True
    for j in range(len(word)):

        idx = int(ord(word[j]) - ord('A'))
        s[idx][0] += 1

        if s[idx][0] == 3:
            if j == len(word) - 1:
                print("FAKE")
                ok = False
                break
            if word[j + 1] != word[j]:
                print("FAKE")
                ok = False
                break
            s[idx][0] = -1

    if ok:
        print("OK")
