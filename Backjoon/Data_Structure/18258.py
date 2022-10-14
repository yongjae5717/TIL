import sys
from collections import deque
input = sys.stdin.readline


def push(lst, num):
    lst.append(num)


def pop(lst):
    if len(lst) != 0:
        print(lst[0])
        lst.popleft()
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
        print(lst[-1])
    else:
        print(-1)


N = int(input())

# list를 사용하면 O(n)으로 시간초과가 나기때문에 deque를 이용해준다.
queue = deque()
for _ in range(N):
    s = input().split()
    command = s[0]
    if command == "push":
        num = s[1]
        push(queue, int(num))
    elif command == "front":
        front(queue)
    elif command == "back":
        back(queue)
    elif command == "size":
        size(queue)
    elif command == "empty":
        empty(queue)
    elif command == "pop":
        pop(queue)