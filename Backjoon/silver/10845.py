import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()


def push(x):
    global q
    q.append(x)


def pop(x):
    global q
    value = -1
    if q:
        value = q.popleft()
    return value


def size():
    global q
    return len(q)


def empty():
    global q
    if len(q) == 0:
        return 1
    return 0


def front():
    global q
    if q:
        return q[0]
    return -1


def back():
    global q
    if q:
        return q[len(q)-1]
    return -1


def solution(n):
    for _ in range(n):
        input_list = list(input().split())
        command, number = "", ""
        if len(input_list) == 1:
            command = input_list[0]
        elif len(input_list) == 2:
            command, number = input_list

        if command == "push":
            push(number)
        elif command == "pop":
            print(pop(number))
        elif command == "size":
            print(size())
        elif command == "empty":
            print(empty())
        elif command == "front":
            print(front())
        elif command == "back":
            print(back())


solution(n)