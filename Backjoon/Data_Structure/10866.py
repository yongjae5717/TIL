import sys
from collections import deque
input = sys.stdin.readline


def push_front(lst, num):
    lst.appendleft(num)


def push_back(lst, num):
    lst.append(num)


def pop_front(lst):
    if len(lst) != 0:
        print(lst.popleft())
    else:
        print(-1)


def pop_back(lst):
    if len(lst) != 0:
        print(lst.pop())
    else:
        print(-1)


def size(lst):
    print(len(lst))


def empty(lst):
    if len(lst) != 0:
        print(0)
    else:
        print(1)


def front(lst):
    if len(lst) != 0:
        print(lst[0])
    else:
        print(-1)


def back(lst):
    if len(lst) != 0:
        print(lst[len(lst)-1])
    else:
        print(-1)


def main():
    N = int(input())
    deck = deque()
    for _ in range(N):
        command = list(map(str, input().split()))
        if command[0] == "push_front":
            push_front(deck, int(command[1]))
        elif command[0] == "push_back":
            push_back(deck, int(command[1]))
        elif command[0] == "pop_front":
            pop_front(deck)
        elif command[0] == "pop_back":
            pop_back(deck)
        elif command[0] == "size":
            size(deck)
        elif command[0] == "empty":
            empty(deck)
        elif command[0] == "front":
            front(deck)
        elif command[0] == "back":
            back(deck)

main()