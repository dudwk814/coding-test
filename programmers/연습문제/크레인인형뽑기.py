def solution(board, moves):
    answer = 0
    array = []

    for i in moves:

        i -= 1

        for j in range((len(board))):
            if board[j][i] != 0:
                array.append(board[j][i])
                board[j][i] = 0
                break

        if len(array) > 1:
            if array[len(array) - 1] == array[len(array) - 2]:
                answer += 2
                array.pop()
                array.pop()

    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
    4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
