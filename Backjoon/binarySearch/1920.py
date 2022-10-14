import sys
import heapq

N = int(sys.stdin.readline())
A = set(sys.stdin.readline().split())
M = int(sys.stdin.readline())
B = list(sys.stdin.readline().split())

# print(A, B)
for i in range(len(B)):
    if B[i] in A:
        print("1")
    else:
        print("0")

