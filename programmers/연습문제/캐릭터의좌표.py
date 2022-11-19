def solution(keyinput, board):
    answer = []

    current_x = 0
    current_y = 0

    boder_x = board[0] // 2
    boder_y = board[1] // 2

    for key in keyinput:
        if key == "up":
            if current_y + 1 > boder_y:
                continue
            current_y += 1
        elif key == "down":
            if current_y - 1 < -boder_y:
                continue
            current_y -= 1
        elif key == "left":
            if current_x - 1 < -boder_x:
                continue
            current_x -= 1
        elif key == "right":
            if current_x + 1 > boder_x:
                continue
            current_x += 1

    answer.append(current_x)
    answer.append(current_y)
    return answer


solution(["left", "right", "up", "right", "right"], [11, 11])

i = 11
i = - 11

print(i)
