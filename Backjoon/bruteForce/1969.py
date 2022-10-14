import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s = list(list(input().strip()) for _ in range(n))

# hamming distance: 각 위치의 문자가 다른 것의 개수
hamming_distance = 0
DNA = [[] for _ in range(m)]
DNA_s = ""

for i in range(m):
    for j in range(n):
        DNA[i].append(s[j][i])

for i in range(m):
    a = DNA[i].count('A')
    t = DNA[i].count('T')
    g = DNA[i].count('G')
    c = DNA[i].count('C')
    max_count = max(a, t, g, c)
    if a == max_count:
        DNA_s += 'A'
    elif c == max_count:
        DNA_s += 'C'
    elif g == max_count:
        DNA_s += 'G'
    elif t == max_count:
        DNA_s += 'T'
print(DNA_s)

for i in range(n):
    compare_s = s[i]
    for j in range(m):
        if DNA_s[j] != compare_s[j]:
            hamming_distance += 1
print(hamming_distance)