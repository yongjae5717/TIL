import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort(reverse=True)
        b.sort()

        count = 0
        for num_a in a:
            for num_b in b:
                if num_a > num_b:
                    count += 1
                else:
                    break
        print(count)


main()