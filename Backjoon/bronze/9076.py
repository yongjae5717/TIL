import sys
input = sys.stdin.readline


def main():
    t = int(input())
    scores = list(list(map(int, input().split())) for _ in range(t))
    for i in range(t):
        scores[i].sort()
        temp = scores[i][1:len(scores[i])-1]
        if temp[-1] - temp[0] >= 4:
            print("KIN")
        else:
            print(sum(temp))


main()
