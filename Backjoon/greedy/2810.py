import sys

N = int(sys.stdin.readline())
array = list(sys.stdin.readline().strip())


count = N + 1
flag = False
for i in array:
    if i == "L" and flag is False:
        count -= 1
        flag = True
    elif i == "L" and flag is True:
        flag = False
if count > N:
    print(N)
else:
    print(count)