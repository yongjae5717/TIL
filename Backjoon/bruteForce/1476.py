import sys

E, S, M = map(int, sys.stdin.readline().split())
# max E = 15, max S = 28, max M = 19

count = 0
while True:
    # print(count)
    count += 1
    if E == S == M:
        print(E)
        break
    if (count % 15 + 1) == E and (count % 28 + 1) == S and (count % 19 + 1) == M:
        print(count + 1)
        break
