# 순환 문자열
s1 = input()
s2 = input()
s3 = input()

if s1[len(s1) - 1] == s2[0]:
    if s2[len(s2) - 1] == s3[0]:
        if s3[len(s3) - 1] == s1[0]:
            print('good')
        else:
            print('bad')    
    else:
        print('bad')    
else:
    print('bad')        