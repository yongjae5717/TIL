import sys

N = sys.stdin.readline().strip()
array = list()

for i in N:
    array.append(i)

array.sort(reverse=True)
result = ""
for j in range(len(array)):
    result += array[j]
print(result)
