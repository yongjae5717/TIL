import sys

N = list(sys.stdin.readline().strip())

number = list([0] * 10)
for i in N:
    if int(i) == 6:
        number[9] += 1
    else:
        number[int(i)] += 1

number[9] = (number[9] + 1) // 2
print(max(number))