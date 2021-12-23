# 사전 자료형: 키와 값의 쌍을 데이터로 가지는 자료형
# 리스트나 튜플과 달리 키와 값 쌍으로 되어 있어 검색 및 수정에 효율적

# 사전 자료형 초기화
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data['사과'])

# key 데이터만 담은 리스트
key_list = data.keys()

# 값 데이터만 담은 리스트
value_list = data.values()

print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in data.keys():
    print(data[key])
