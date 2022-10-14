import sys


N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
result = list()
for i in array:
    if i not in result:
        result.append(i)

result.sort()
result_string = ""
for j in result:
    result_string += str(j) + " "

print(result_string)