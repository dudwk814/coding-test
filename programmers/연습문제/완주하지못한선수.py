def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    for i in range(len(participant)):
        if i == len(participant) - 1:
            answer = participant[i]
            break

        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer


print(solution(["mislav", "stanko", "mislav", "ana"],
      ["stanko", "ana", "mislav"]))
