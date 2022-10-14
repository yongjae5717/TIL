import sys

N, K = map(int, sys.stdin.readline().split())
array = list(i+1 for i in range(N))
result = list()
# print(array)
count = 0


while array:
    count = (count + K - 1) % len(array)
    result.append(str(array.pop(count)))

print("<"+", ".join(result)+">")