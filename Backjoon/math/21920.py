import sys, math
input = sys.stdin.readline

# 서로소: 1을 제외한 나머지 공약수중 곂치는것이 없는 수
n = int(input())
a = list(map(int, input().split()))
x = int(input())

result = list()
for i in a:
    gcd = math.gcd(i, x)
    if gcd == 1:
        result.append(i)

print(sum(result) / len(result))