"""
# list를 이용하면 시간초과
import sys

N, K = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().strip()))
count = 0
while count != K:
    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            # print(array[i], array[i-1])
            del array[i-1]
            count += 1
            break

result = ""
for j in array:
    result += str(j)
print(result)
"""

# stack 이용
import sys

N, K = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().strip()))
stack = []
temp_k = K
for i in range(N):
    while len(stack) > 0 and K > 0:
        if stack[-1] < array[i]:
            del stack[-1]
            K -= 1
        else:
            break
    stack.append(array[i])

result = ""
count = 0
for i in stack:
    if count != N-temp_k:
        result += str(i)
        count += 1
print(result)