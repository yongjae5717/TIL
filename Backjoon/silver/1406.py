import sys
from collections import deque
input = sys.stdin.readline


def solution():
    q = deque(input().strip())
    m = int(input())
    current_loc = len(q)
    for _ in range(m):
        input_list = list(input().split())
        command = input_list[0]
        if command == 'L':
            if current_loc > 0:
                q.appendleft(q.pop())
                current_loc -= 1
        elif command == 'D':
            if current_loc < len(q):
                q.append(q.popleft())
                current_loc += 1
        elif command == 'B':
            if current_loc > 0:
                q.pop()
                current_loc -= 1
        elif command == 'P':
            q.append(input_list[1])
            current_loc += 1
    for _ in range(len(q) - current_loc):
        q.append(q.popleft())
    return list(q)


def main():
    result_list = solution()
    print("".join(result_list))


main()