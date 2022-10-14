import sys

N, M = map(int, sys.stdin.readline().split())

cannot_hear = set(sys.stdin.readline().strip() for _ in range(N))
cannot_hear_and_see = list()
for i in range(M):
    temp = sys.stdin.readline().strip()
    if temp in cannot_hear:
        cannot_hear_and_see.append(temp)

cannot_hear_and_see.sort()

print(len(cannot_hear_and_see))

for j in cannot_hear_and_see:
    print(j)