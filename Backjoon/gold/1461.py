import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    book = list(map(int, input().split()))

    # +, -을 분리해서 position 구간별로 나눈다.
    plus_position = []
    minus_position = []
    count = []

    for i in book:
        if i > 0:
            plus_position.append(i)
        else:
            minus_position.append(abs(i))

    # 내림차순으로 정렬
    plus_position.sort(reverse=True)
    minus_position.sort(reverse=True)

    for i in range(len(plus_position) // m):
        count.append(plus_position[i * m])
    if len(plus_position) % m > 0:
        count.append(plus_position[(len(plus_position) // m) * m])

    for i in range(len(minus_position) // m):
        count.append(minus_position[i * m])
    if len(minus_position) % m > 0:
        count.append(minus_position[(len(minus_position) // m) * m])

    count.sort()

    result = count.pop()
    result += 2 * sum(count)

    print(result)


main()