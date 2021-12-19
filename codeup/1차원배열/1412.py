# 알파벳 개수 출력하기
s = input()

for i in range(ord('a'), ord('z') + 1):
    count = s.count(chr(i))

    print(chr(i), count, sep=':')
