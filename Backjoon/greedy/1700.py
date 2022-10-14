import sys


def main():
    N, K = map(int, sys.stdin.readline().split())

    seq = list(map(int, sys.stdin.readline().split()))

    multi = list()
    for i in range(N):
        multi.append(0)

    result, count, flag = 0, 0, 0
    for i in range(K):
        print(multi, seq, result)
        if seq[i] not in multi and count != N:
            multi[count] = seq[i]
            seq[i] = 0
            count += 1
        elif seq[i] in multi:
            # print("case1:", seq[i])
            seq[i] = 0
        else:
            flag2 = 0
            for j in range(N):
                if multi[j] not in seq:
                    multi[j] = seq[i]
                    flag2 = 1
                    break
            if flag2 == 0:
                multi[0] = seq[i]
            seq[i] = 0
            result += 1
            # print("case2:", seq[i])
    print(multi, seq, result)
    # print(result)


main()