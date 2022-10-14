import sys

N, K = map(int, sys.stdin.readline().split())
PH = list(sys.stdin.readline().strip())
# print(PH)
result = 0
for i in range(N):
    if PH[i] == "P":
        for j in range(max(i-K, 0), min(i+K+1, N)):
            if PH[j] == "H":
                PH[j] = "X"
                result += 1
                break

print(result)