# Problem 11047
# 준규가 가지고 있는 동전은 총 N 종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을
# 구하는 프로그램을 작성하시오.

# Input
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다.
# (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

# Output
# 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

import sys


def main():
    N, K = sys.stdin.readline().split()
    N = int(N)
    K = int(K)
    list_coin = []
    total = 0
    for i in range(N):
        list_coin.append(int(sys.stdin.readline()))
    for i in range(N):
        if K // int(list_coin[N-i-1]) > 0:
            total += K // int(list_coin[N-i-1])
            K = K % int(list_coin[N-i-1])
    print(total)


main()