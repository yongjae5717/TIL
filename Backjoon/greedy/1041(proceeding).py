import sys

N = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split()))
array.sort()

# 주사위의 개수: N^3
# 2 -> 동일한 주사위 8개
# 2 -> 총 4 * 5
# 3 -> 총 9 * 5
# N -> 총 N^2 * 5

# 총 면 개수: N^2 * 5
# 윗면 대각선 개수: 4개 x 3
# 옆면 대각선 개수: (N - 1) x 2 x 4
# 윗면 끝 개수: (N-2) * 4
# 나머지 면 개수:
total = N * N * 5
up = 12
side = (N-1) * 2 * 4
up_side = (N-2) * 4
result1 = (total - up - side - up_side) * array[0]\
          + 4 * (array[0] + array[1] + array[2])\
          + (side // 2) * (array[0] + array[1])\
          + up_side * (array[0] + array[1])
