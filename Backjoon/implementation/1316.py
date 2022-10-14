import sys

N = int(sys.stdin.readline())
array = list(sys.stdin.readline().strip() for _ in range(N))
count = N
for i in array:
    dictionary = dict()
    temp = ""
    for j in i:
        if j not in dictionary:
            dictionary[j] = 1
            temp = j
        elif j in dictionary and j != temp:
            count -= 1
            break

print(count)