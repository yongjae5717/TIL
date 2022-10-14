import sys

N, M = map(int, sys.stdin.readline().split())

array_1 = list(sys.stdin.readline().split())
array_1 += sys.stdin.readline().split()
for i in range(len(array_1)):
    array_1[i] = int(array_1[i])
array_1.sort()

result = ""
for j in array_1:
    result += str(j) + " "
print(result)