import sys
input = sys.stdin.readline

N = int(input())
stack = list()


def push(stack, num):
    stack.append(num)


def pop(stack):
    if len(stack) != 0:
        n = stack[len(stack)-1]
        print(n)
        del stack[-1]
    else:
        print(-1)


def size(stack):
    print(len(stack))


def empty(stack):
    if len(stack) == 0:
        print(1)
    else:
        print(0)


def top(stack):
    if len(stack) != 0:
        print(stack[len(stack)-1])
    else:
        print(-1)


for _ in range(N):
    command = input().strip()
    num = 0
    if len(command) > 5:
        command, num = command.split()
    if command == "push":
        push(stack, num)
    elif command == "top":
        top(stack)
    elif command == "size":
        size(stack)
    elif command == "empty":
        empty(stack)
    elif command == "pop":
        pop(stack)
