import sys


def pal(dict):
    global result
    count = 0
    odd_count = 0
    odd = False
    for i in dict:
        if dict[i] % 2 == 1:
            odd_count += 1
        if dict[i] % 2 == 1 and odd is False:
            result = i
            dict[i] -= 1
            odd = True
    if odd_count > 1:
        result = "I'm Sorry Hansoo"
        return
    for i in dict:
        for _ in range(dict[i]):
            if count % 2 == 0:
                result = i + result
                count += 1
            else:
                result = result + i
                count += 1
    return


name = list(map(str, sys.stdin.readline().rstrip()))
name.sort(reverse=True)
temp = dict()
result = ""
for i in name:
    if i not in temp:
        temp[i] = 1
    else:
        temp[i] += 1

pal(temp)
print(result)