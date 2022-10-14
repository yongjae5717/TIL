import sys


N = int(sys.stdin.readline())
array = list()
count = 0
for _ in range(N):
    temp, name = sys.stdin.readline().split()
    old = int(temp)
    count += 1
    array.append((old, name, count))

array.sort(key=lambda x: (x[0], x[2]))

for i in array:
    print(i[0], i[1])