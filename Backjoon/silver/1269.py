import sys
input = sys.stdin.readline
a, b = map(int, input().split())

aSet = set(map(int, input().split()))
bSet = set(map(int, input().split()))


def solution(set1, set2):
    diff1to2 = set1 - set2
    diff2to1 = set2 - set1
    return len(diff1to2) + len(diff2to1)


print(solution(aSet, bSet))