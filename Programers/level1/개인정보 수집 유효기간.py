def solution(today, terms, privacies):
    answer = []
    agreements = dict()
    today_cal = day_calculator(today, 0)
    for t in terms:
        type, period = t.split()
        if type not in agreements:
            agreements[type] = int(period)

    p_list = list()
    for p in privacies:
        day, agreement = p.split()
        p_list.append(day_calculator(day, agreements[agreement]))

    count = 1
    for p in p_list:
        if today_cal[0] > p[0]:
            answer.append(count)
        elif today_cal[0] == p[0] and today_cal[1] >= p[1]:
            answer.append(count)
        count += 1

    return answer


def day_calculator(day, month):
    day_list = list(map(int, day.split(".")))
    m = day_list[0] * 12 + day_list[1] + month
    d = day_list[2]
    return [m, d]


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))