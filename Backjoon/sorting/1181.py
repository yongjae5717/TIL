import sys

N = int(sys.stdin.readline())

array = list()
for _ in range(N):
    name = sys.stdin.readline().strip()
    if name not in array:
        array.append(name)

array.sort()
array.sort(key=lambda x: len(x))
# print(array)

for i in array:
    print(i)