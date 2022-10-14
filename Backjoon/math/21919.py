import sys, math
# use queue
from collections import deque
input = sys.stdin.readline


# prime function: return True or False ( bool )
def is_prime(num):
    if num == 1:
        return False
    if num % 2 == 0:
        if num == 2:
            return True
        return False
    for i in range(3, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


n = int(input())
a = list(map(int, input().split()))
prime_num = deque()
for i in a:
    if is_prime(i):
        prime_num.appendleft(i)

if prime_num:
    for i in range(len(prime_num)-1):
        if len(prime_num) >= 2:
            x = prime_num.popleft()
            y = prime_num.popleft()
            prime_num.appendleft(x * y // math.gcd(x, y))
    print(prime_num.pop())
else:
    print(-1)