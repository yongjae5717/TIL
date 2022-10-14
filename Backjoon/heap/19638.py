"""
뿅망치에 맞은 사람의 키: 뽕망치에 맞은 사람의 키 / 2 (키가 1인 경우는 변함이 없다)
뿅망치를 효율적으로 사용하기 위한 전략
1. 바로 매번 가장 키가 큰 거인 가운데 하나를 때리는 것이다.
N: 인구수
H: 센티의 키
T: 뿅망치 횟수 제한

거인의 나라에 모든 거인이 센티보다 키가 작다면 YES, 아니라면 NO 출력

YES: 뿅망치를 최소 사용한 횟수 출력
NO:뿅망치 사용한 이후 가장 큰 거인의 키 출력

우선순위 큐를 사용
"""

import sys
import heapq


def check(lst):
    global H
    temp = int(heapq.heappop(lst) * (-1))
    if temp < H:
        return True
    heapq.heappush(lst, -temp)
    return False


N, H, T = map(int, sys.stdin.readline().split())
people = list()
flag = False
count = 0

for _ in range(N):
    heapq.heappush(people, -int(sys.stdin.readline()))

for _ in range(T):
    flag = check(people)
    if flag:
        break
    temp = int(heapq.heappop(people) * (-1) / 2)
    count += 1
    if temp < 1 and H != 1:
        flag = True
        heapq.heappush(people, -1)
    elif temp < 1 and H == 1:
        heapq.heappush(people, -1)
    else:
        heapq.heappush(people, -temp)
        flag = check(people)


if flag:
    print("YES")
    print(count)
else:
    print("NO")
    print(-heapq.heappop(people))