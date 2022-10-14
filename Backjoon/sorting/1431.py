import sys

N = int(sys.stdin.readline())

array = list()
for _ in range(N):
    serial = sys.stdin.readline().strip()
    count = 0
    for i in serial:
        if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" \
                or i == "6" or i == "7" or i == "8" or i == "9":
            count += int(i)
    array.append((serial, len(serial), count))

array.sort()
array.sort(key=lambda x: (x[1], x[2]))
for i in array:
    print(i[0])