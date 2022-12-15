import sys
from collections import deque
input = sys.stdin.readline


def reverse_list(lst):
    return list(reversed("".join(lst)))


def main():
    t = int(input())
    for _ in range(t):
        flag = False
        p = list(input().strip())
        n = int(input())
        input_string1 = str(input().strip())
        if input_string1[0] != "[" or input_string1[-1] != "]":
            print("error")
            continue

        input_string = input_string1.replace("[", "").replace("]", "")
        array = input_string.strip().split(",")
        if n != len(array):
            print("error")
            continue

        if len(array) == 1 and array[0] == '' and p.count("D") != 0:
            print("error")
            continue

        q = deque(array)
        count = 0
        for c in p:
            if c == 'R':
                count += 1
            elif c == 'D':
                if q:
                    if count % 2 == 1:
                        q.pop()
                    else:
                        q.popleft()
                else:
                    flag = True
                    break

        if count % 2 == 1:
            q = deque(reverse_list(list(q)))

        if flag is False:
            result = " ".join(list(q))
            result_list = list(map(int, result.split()))
            print(str(result_list).replace(" ", ""))
        else:
            print("error")


main()