import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort(reverse=True)
days = 0
last_days = 1 + len(array) + array[len(array)-1]

for i in range(len(array)):
    if days <= (array[i] + i):
        days = array[i] + i
        # print(days, i)
days = days + 2
if last_days > days:
    days = last_days

print(days)