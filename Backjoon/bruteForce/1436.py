import sys

N = int(sys.stdin.readline())

count = 0
i = 0
while count != N:
    i += 1
    number = str(i)
    if "666" in number:
        count += 1
    if count == N:
        print(number)