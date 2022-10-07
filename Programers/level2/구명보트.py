from collections import deque


def solution(people, limit):
    result = 0
    q = deque()
    people.sort()
    for i in people:
        q.append(i)

    x, y = q.popleft(), q.popleft()
    if x + y > limit:
        return len(people)
    elif x + y == limit:
        return len(people) - 1
    else:
        q.appendleft(y)
        q.appendleft(x)
        while q:
            if len(q) == 1:
                result += 1
                break
            x, y = q.popleft(), q.pop()
            if x + y <= limit:
                result += 1
            else:
                result += 1
                q.appendleft(x)
        return result