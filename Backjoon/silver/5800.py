import sys
input = sys.stdin.readline


def main():
    k = int(input())
    math_scores = list(list(map(int, input().split())) for _ in range(k))
    count = 0
    for math_score in math_scores:
        count += 1
        n, score = math_score[0], math_score[1:]
        score.sort()
        print("Class", count)
        gap = 0
        for i in range(1, n):
            gap = max(gap, score[i] - score[i-1])

        print("Max %d, Min %d, Largest gap %d" %(score[-1], score[0], gap))


main()