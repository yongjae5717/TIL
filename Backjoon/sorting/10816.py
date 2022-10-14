import sys

N = int(sys.stdin.readline())
array_1 = list(sys.stdin.readline().split())
M = int(sys.stdin.readline())
array_2 = list(sys.stdin.readline().split())
count = 0
# print(array_2)
dict_1 = dict()
for i in array_1:
    if i not in dict_1:
        dict_1[i] = 1
    else:
        dict_1[i] += 1

result = ""
for i in array_2:
    if i in dict_1:
        result += str(dict_1[i]) + " "
    else:
        result += "0 "
print(result)