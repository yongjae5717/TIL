import sys

K = int(sys.stdin.readline())
stack = list()
for _ in range(K):
    stack.append(int(sys.stdin.readline()))
    if stack[len(stack) - 1] == 0:
        stack.pop()
        stack.pop()

print(sum(stack))