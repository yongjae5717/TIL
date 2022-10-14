import queue
import sys

test_case = int(sys.stdin.readline())
result = list()
for _ in range(test_case):
    N, M = map(int, sys.stdin.readline().split())
    sig = list(map(int, sys.stdin.readline().split()))
    order = list(["False"] * N)
    order[M] = "True"
    count = 0

    while True:
        if sig[0] == max(sig):
            count += 1
            if order[0] == "True":
                result.append(count)
                break
            else:
                sig.pop(0)
                order.pop(0)
        else:
            sig.append(sig.pop(0))
            order.append(order.pop(0))

for s in result:
    print(s)