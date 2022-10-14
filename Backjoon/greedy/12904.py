import sys

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()


def compare(S, T):
    if len(S) < len(T):
        while len(T) != len(S):
            if T[len(T)-1] == 'A':
                T = T[:len(T)-1]
            elif T[len(T)-1] == "B":
                T = T[:len(T)-1]
                T = T[::-1]
        return T


result = compare(S, T)
# print(S, result)
if S == result:
    print(1)
else:
    print(0)