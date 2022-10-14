import sys
input = sys.stdin.readline

n = int(input())
energy_drinks = list(map(int, input().split()))
energy_drinks.sort()
result = energy_drinks[n-1]

for i in range(n-1):
    result += energy_drinks[i] / 2

print(result)