import sys
from collections import deque
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    nums = deque(map(int, input().split()))
    q = deque(list(i for i in range(1, n+1)))

    count = 0
    while nums:
        temp_nums = deque(nums)
        temp_q = deque(q)
        temp_nums2 = deque(nums)
        temp_q2 = deque(q)
        left = left_move (temp_nums, 0, temp_q)
        right = right_move(temp_nums2, 0, temp_q2)
        if left < right:
            nums, q = deque(temp_nums2), deque(temp_q2)
        else:
            nums, q = deque(temp_nums), deque(temp_q)
        count += min(left, right)

    print(count)


def left_move(temp_nums, temp_count, temp_q):
    while temp_nums[0] != temp_q[0]:
        temp_q.append (temp_q.popleft ())
        temp_count += 1
    temp_q.popleft ()
    temp_nums.popleft ()
    return temp_count


def right_move(nums, count, q):
    while nums[0] != q[0]:
        q.appendleft (q.pop ())
        count += 1
    q.popleft ()
    nums.popleft ()
    return count


main()