import sys
from math import gcd
input = sys.stdin.readline


def solution(n, plant_distance, gcd_value):
    result = 1
    for p in plant_distance:
        result += p // gcd_value

    return result - n


def main():
    n = int(input())
    plant_distance = list()
    temp1 = int(input())
    gcd_value = 0
    for i in range(1, n):
        temp2 = int(input())
        distance = temp2 - temp1
        plant_distance.append(distance)
        gcd_value = gcd(gcd_value, distance)
        temp1 = temp2

    answer = solution(n, plant_distance, gcd_value)
    print(answer)


main()