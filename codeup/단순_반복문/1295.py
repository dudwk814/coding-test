# 주어지는 문장의 대문자를 소문자로, 소문자를 대문자로 변경하는 프로그램을 작성
# a ~ z = 97 ~ 122
# A ~ Z = 65 ~ 90
s = input()
w = ""

for i in range(len(s)):
    if ord(s[i]) >= 65 and ord(s[i]) <= 90:  # s[i]를 아스키코드로 변환한 값이 65 ~ 90 사이면 대문자
        w += s[i].lower()
    elif ord(s[i]) >= 97 and ord(s[i]) <= 122:  # s[i]를 아스키코드로 변환한 값이 97 ~ 122 사이면 소문자
        w += s[i].upper()
    else:   # 그 외(숫자 등)면 그대로 저장
        w += s[i]

print(w)
