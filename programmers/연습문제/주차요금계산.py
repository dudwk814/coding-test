import math
from datetime import datetime


def solution(fees, records):
    basic_time = fees[0]
    basic_charge = fees[1]
    unit_time = fees[2]
    unit_charge = fees[3]

    answer = []
    cars = {}

    for i in range(len(records)):
        time, num, act = records[i].split()
        if cars.get(num) == None:
            cars[num] = {'time': []}
        cars[num]['time'].append(time)

    keys = cars.keys()

    for key in keys:
        times = cars[key]['time']
        if len(times) % 2 != 0:
            times.append("23:59")
        time = 0

        for i in range(0, len(times), + 2):
            time1 = times[i]
            time2 = times[i + 1]
            time_sub = datetime.strptime(time2, "%H:%M") - \
                datetime.strptime(time1, "%H:%M")

            time_sub = str(time_sub)

            time_sub = time_sub[:-3]
            h, m = time_sub.split(":")
            time += (int(h) * 60) + int(m)

        sub_time = 0
        charge = 0
        if time > basic_time:
            sub_time = (time - basic_time) / unit_time
            if (time - basic_time) / unit_time % unit_time != 0:
                sub_time = math.ceil(sub_time)

        charge = basic_charge + (sub_time * unit_charge)

        answer.append((charge, key))

    answer.sort(key=lambda x: x[1])
    for i in range(len(answer)):
        answer[i] = answer[i][0]
    return answer


solution([1, 461, 1, 10, 5000, 10, 600],
         ["00:00 1234 IN"])
