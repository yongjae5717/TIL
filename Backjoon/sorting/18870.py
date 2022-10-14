import sys

N = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split()))
sort_array = list()

for i in array:
    sort_array.append(i)

sort_array.sort()
dictionary = dict()
count = 0

for i in range(N):
    if sort_array[i] not in dictionary:
        dictionary[sort_array[i]] = count
        count += 1

result = ""
for j in array:
    result += str(dictionary[j]) + " "

print(result)