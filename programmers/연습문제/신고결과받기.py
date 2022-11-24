def solution(id_list, report, k):
    answer = []
    array = {}

    for i in range(len(id_list)):
        array[id_list[i]] = {'count': 0, 'id': [], 'idx': 0}
        id_list[i] = [id_list[i], 0]

    for i in range(len(report)):
        user_id, reported_id = report[i].split()

        if user_id in array[reported_id]['id']:
            continue
        else:
            array[reported_id]['count'] = array[reported_id]['count'] + 1
            array[reported_id]['id'].append(user_id)

    keys = list(array.keys())
    for key in keys:
        if array[key]['count'] >= k:
            users = array[key]['id']
            for user in users:
                array[user]['idx'] += 1
    for key in keys:
        answer.append(array[key]['idx'])
    return answer


solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo",
         "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)
