import sys


N = int(sys.stdin.readline())
array = list(int(sys.stdin.readline()) for _ in range(N))
array.sort()
dictionary = dict()
for i in array:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1
for j in dictionary:
    if dictionary[j] == max(dictionary.values()):
        print(j)
        break
