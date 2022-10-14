import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
city = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

# 0: 빈 칸, 1: 집, 2: 치킨집
# 치킨거리: 집과 가장 가까운 치킨집 사이의 거리
# ex) (2, 1)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |2-1| + |1-2| = 2

house, chicken = list(), list()

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])


result = 1000000
for chick in combinations(chicken, M):
    s = 0
    for h in house:
        chick_to_house = 1000000
        for n in range(M):
            chick_to_house = min(chick_to_house, abs(h[0] - chick[n][0]) + abs(h[1] - chick[n][1]))
        s += chick_to_house
    result = min(result, s)


print(result)