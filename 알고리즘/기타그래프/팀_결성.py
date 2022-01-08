# 특정 원소에 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (n + 1)

# 부모 테이블의 값을 자기 자신으로 초기화
for i in range(n + 1):
    parent[i] = i

# 연산의 횟수 만큼 반복하며, find_parent, union_parent 수행 
for i in range(m):
    oper, a, b = map(int, input().split())

    if oper == 0: # 연산이 0이라면 합치기 연산
        union_parent(parent, a, b)
    else: # 연산이 0이 아니라면 같은 팀 여부 연산
        a = find_parent(parent, a)
        b = find_parent(parent, b)

        if a == b: # 부모 노드가 같다면 같은 집합이므로 YES 출력
            print('YES')
        else: # 부모 노드가 다르다면 같은 집합이 아니므로 NO 출력
            print('NO')    
            

