import sys
input = sys.stdin.readline


def main():
    x, y = input().split()
    len_x, len_y = len(x), len(y)
    result = 51
    if len_x > len_y:
        for i in range(len_x - len_y + 1):
            temp = x[i:i+len_y]
            count = 0
            for j in range(len_y):
                if temp[j] != y[j]:
                    count += 1
            result = min(result, count)
    elif len_y > len_x:
        for i in range(len_y - len_x + 1):
            temp = y[i:i+len_x]
            count = 0
            for j in range(len_x):
                if temp[j] != x[j]:
                    count += 1
            result = min(result, count)
    else:
        count = 0
        for i in range(len_x):
            if x[i] != y[i]:
                count += 1
        result = count

    return result


print(main())