import sys
input = sys.stdin.readline

a, b, c, m = map(int, input().split())

tired, day, work = 0, 0, 0
while day < 24:
    day += 1
    if tired + a <= m:
        tired += a
        work += b
    else:
        tired -= c

    if tired <= 0:
        tired = 0

print(work)