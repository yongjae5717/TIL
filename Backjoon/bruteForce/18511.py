import sys
# 중복을 허용하는 조합
from itertools import product

input = sys.stdin.readline

n, k = map(int, input().split())

lst = list(map(int, input().split()))
# 큰수부터 정렬(오름차순)
lst.sort(reverse=True)

result = 0
flag = False
length = len(str(n))
while flag is False:
    for i in product(lst, repeat=length):
        temp = 0
        for j in i:
            temp = temp * 10 + j
        if temp <= n:
            flag = True
            print(temp)
            break
    if flag:
        break
    length -= 1