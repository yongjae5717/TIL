import sys
input = sys.stdin.readline

n = int(input())
temp = n
flag = False
count = 0

if int(n / 5) > 0:
    count += int(n / 5)
    n = n - 5 * int(n / 5)

while n != 0:
    if n % 2 == 0:
        count += int(n / 2)
        n = n - 2 * int(n / 2)
    else:
        count -= 1
        n += 5
        if temp < n:
            flag = True

if flag:
    print(-1)
else:
    print(count)