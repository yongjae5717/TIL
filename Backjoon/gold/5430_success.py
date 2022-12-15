import sys
from collections import deque
input = sys.stdin.readline


def main():

    t = int(input())

    for i in range(t):

        # parsing
        p = sys.stdin.readline().rstrip()
        n = int(input())
        array = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

        if n == 0:
            array = deque()

        flag = False
        count = 0
        for j in p:
            if j == 'R':
                count += 1
            elif j == 'D':
                if array:
                    if count % 2 == 1:
                        array.pop()
                    else:
                        array.popleft()
                else:
                    print("error")
                    flag = True
                    break

        if count % 2 == 1:
            array.reverse()

        if flag == 0:
            print(str(list(array)).replace(" ", "").replace("'", ""))


main()