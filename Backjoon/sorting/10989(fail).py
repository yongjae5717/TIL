import sys
input = sys.stdin.readline

n = int(input())
array = [0] * 10001

for _ in range(n):
    array[int(input())] += 1

for i in range(10001):
    num = i
    if array[i] != 0:
        for _ in range(array[i]):
            sys.stdout.write(str(i) + "\n")