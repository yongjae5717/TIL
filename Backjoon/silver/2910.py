import sys
input = sys.stdin.readline


def main():
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))

    result = list()
    check = [0] * (max(arr) + 1)

    for i in arr:
        if check[i] == 0:
            check[i] = 1
            result.append((i, arr.count(i)))
    result.sort(key=lambda x: x[1], reverse=True)

    answer = list()
    for r in result:
        value, count = r
        answer += [value] * count

    print(* answer)


main()