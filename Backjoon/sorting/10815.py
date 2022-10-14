import sys

N = int(sys.stdin.readline())
array_N = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
array_M = list(map(int, sys.stdin.readline().split()))

dictionary = dict()
for i in array_N:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1

result = ""
for j in array_M:
    if j in dictionary:
        result += str(dictionary[j]) + " "
    else:
        result += str(0) + " "

print(result)