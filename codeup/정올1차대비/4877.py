a, b, c, n = map(int, input().split())
is_find = False
if n % c == 0:
    is_find = True
elif n % b == 0:
    is_find = True
elif n % a == 0:
    is_find = True
else:

    for i in range(0, n + 1, c):

        if is_find:
            break
        result = i

        for j in range(0, n + 1, b):
            if result < n:
                result += j
            elif result > n:
                break

            if result == n:
                is_find = True

                break
            for k in range(0, n + 1, a):
                if result < n:
                    result += a
                elif result > n:
                    break

                if result == n:
                    is_find = True
                    break
if is_find:
    print(1)
else:
    print(0)
