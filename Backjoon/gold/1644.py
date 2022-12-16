import sys
input = sys.stdin.readline


def solution():
    n = int(input())
    prime_numbers = list()
    for i in range(2, n + 1):

        prime = True
        for j in range(2, int(int(i) ** 0.5) + 1):
            if int(i) % j == 0:
                prime = False
                break
        if prime:
            prime_numbers.append(i)

    count, s, end = 0, 0, 0
    for start in range(len(prime_numbers)):
        while s < n and end < len(prime_numbers):
            s += prime_numbers[end]
            end += 1
        if s == n:
            count += 1
        s -= prime_numbers[start]
    return count


print(solution())