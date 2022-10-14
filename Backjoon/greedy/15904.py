import sys

inp = sys.stdin.readline().strip()
result = ""
flag = 1
inp = inp[::-1]
for i in inp:
    if i.isupper():
        if i == "C" and flag == 1:
            result += i
            flag += 1
        elif i == "P" and flag == 2:
            result += i
            flag += 1
        elif i == "C" and flag == 3:
            result += i
            flag += 1
        elif i == "U" and flag == 4:
            result += i
            flag += 1

# print(result)
if result == "CPCU":
    print("I love UCPC")
else:
    print("I hate UCPC")