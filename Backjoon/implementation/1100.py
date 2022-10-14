import sys

count = 0
array = list(list(sys.stdin.readline().strip())for _ in range(8))
for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0:
            if array[i][j] == "F":
                count += 1
        elif i % 2 == 1 and j % 2 == 1:
            if array[i][j] == "F":
                count += 1

print(count)