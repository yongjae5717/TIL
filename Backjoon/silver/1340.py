import sys
input = sys.stdin.readline


def main():
    month = {"January": 1, "February": 2, "March": 3, "April": 4,
             "May": 5, "June": 6, "July": 7, "August": 8,
             "September": 9, "October": 10, "November": 11, "December": 12}

    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    s = input().strip().replace(",", " ").replace(":", " ")
    tmp = s.split()
    m = tmp[0]
    d, y, hour, minute = map(int, tmp[1:])
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        day[1] += 1
    total_time = sum(day) * 24 * 60
    last_month = month[m] - 1
    current_time = (sum(day[:last_month]) + d - 1) * 24 * 60 + hour * 60 + minute
    print(current_time / total_time * 100)


main()