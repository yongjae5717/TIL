import sys
from math import gcd
input = sys.stdin.readline


def main():
    n, m = map(int, input().split(':'))
    gcd_value = gcd(n, m)
    print(str(n//gcd_value) + ":" + str(m//gcd_value))


main()