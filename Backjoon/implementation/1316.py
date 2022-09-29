import sys
input = sys.stdin.readline

n = int(input())
result = 0
for _ in range(n):
    text = list(input().strip())
    # print(text)
    temp = ""
    flag = False
    dictionary = dict()
    for c in text:
        if c not in dictionary:
            dictionary[c] = 1
        else:
            if temp == c:
                continue
            else:
                flag = True
                break
        temp = c
        print(dictionary)

    if flag is False:
        result += 1

print(result)