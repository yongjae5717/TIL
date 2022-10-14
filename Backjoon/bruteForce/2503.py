import sys
# 순열 사용
from itertools import permutations
input = sys.stdin.readline

n = int(input())
# 모든 경우의 수
num_list = list(permutations(list(i for i in range(1, 10)), 3))

for i in range(n):
    num, s, b = map(int, input().split())
    num = list(str(num))
    count = 0
    # 모든 경우의 수에서 Strike와 Ball의 카운트가 하나라도 다를 경우에 모든 경우의 수 에서 소거
    for j in range(len(num_list)):
        s_count, b_count = 0, 0
        j -= count
        for k in range(3):
            if int(num[k]) in num_list[j]:
                if int(num[k]) == int(num_list[j][k]):
                    s_count += 1
                else:
                    b_count += 1
        if s_count != s or b_count != b:
            num_list.remove(num_list[j])
            count += 1

print(len(num_list))