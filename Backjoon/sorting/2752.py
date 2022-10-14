import sys

a = list(map(int, sys.stdin.readline().split()))

a.sort()

result = ""
for i in a:
    result += str(i) + " "

print(result)