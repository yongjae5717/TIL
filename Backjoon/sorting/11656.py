import sys

inp = sys.stdin.readline().strip()
array = list()
for i in range(len(inp)):
    array.append(inp[i:])

array.sort()
for j in array:
    print(j)