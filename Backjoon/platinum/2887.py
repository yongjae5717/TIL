"""
find연산: 부모 노드를 찾을 때까지 재귀적으로 호출한다.
union연산: 두 원소의 부모 노드를 찾고 번호가 큰 노드가 번호가 작은 노드의 부모를 가리크도록 한다.
이를 효과적으로 수행하기 위해 '부모 테이블'을 항상 가지고 있어야 한다.
"""
import sys
input = sys.stdin.readline

n = int(input())
point = list(list() for _ in range(3))
parents = list(i for i in range(n + 1))


# 특정 원소가 속한 집합을 찾기
def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def main():
    for i in range(n):
        x, y, z = map(int, input().split())
        point[0].append((x, i))
        point[1].append((y, i))
        point[2].append((z, i))

    for i in range(3):
        point[i].sort()

    edges = []
    for curList in point[0], point[1], point[2]:
        # print(curList)
        for i in range(1, n):
            w1, a = curList[i - 1]
            w2, b = curList[i]
            edges.append((abs(w1 - w2), a, b))
            # print(edges)
    edges.sort(reverse=True)
    # print(edges)

    count, result = n-1, 0
    while count:
        w, a, b = edges.pop()
        if find(a) == find(b):
            continue
        union(a, b)
        count -= 1
        result += w

    print(result)


main()