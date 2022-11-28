from collections import deque


def solution(subway, start, end):
    answer = 0
    start_line = 0
    array = [[0]]
    max_num = 0
    for i in range(len(subway)):
        arr = list(map(int, subway[i].split()))
        if arr[0] == start:
            start_line = i + 1

        array.append(arr)
        max_num = max(arr)

    queue = deque([start_line])

    visited = [False] * (max_num + 1)
    visited_line = [False] * (len(array) + 1)

    visited[start] = True
    visited_line[start_line] = True

    while queue:
        v = queue.popleft()  # 현재 역

        print(v, end=' ')

        for i in array[v]:
            if not visited[i]:
                for j in range(1, len(array)):
                    if i in array[j] and not visited_line[j]:
                        queue.append(j)
                        visited[i] = True
                        visited_line[j] = True

    return answer


solution(["1 2 3 4 5 6 7 8", "2 11", "0 11 10",
         "3 17 19 12 13 9 14 15 10", "20 2 21"], 1, 9)
