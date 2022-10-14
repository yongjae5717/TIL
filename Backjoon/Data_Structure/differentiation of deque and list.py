print('deque start')
from collections import deque
a = deque(range(300000))
for i in range(len(a)):
    a.popleft()
print('deque end')

print()

print('list start')
a = list(range(300000))
for i in range(len(a)):
    a.pop(0)
print('list end')