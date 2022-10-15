def solution(fees, records):
    in_out_records = list()
    for i in records:
        time, carNumber, inout = i.split()
        time = int(time[:2]) * 60 + int(time[3:5])
        in_out_records.append([carNumber, time, inout])
    in_out_records.sort(key=lambda x: [x[0], x[1]])

    car_list = dict()
    for i in in_out_records:
        carNumber, time, inout = i
        if carNumber not in car_list:
            car_list[carNumber] = 1439 - time
        else:
            if inout == "IN":
                car_list[carNumber] += 1439 - time
            elif inout == "OUT":
                car_list[carNumber] -= 1439 - time

    lst = [i for i in car_list.values()]

    result = list()

    for i in lst:
        if i <= fees[0]:
            fee = fees[1]
        else:
            if (i - fees[0]) % fees[2] == 0:
                fee = fees[1] + int(((i - fees[0])/fees[2])) * fees[3]
            else:
                fee = fees[1] + (int(((i - fees[0]) / fees[2]))+1) * fees[3]
        result.append(fee)

    return result