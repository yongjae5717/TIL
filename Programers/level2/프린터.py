from collections import deque


def solution(priorities, location):
    # queue를 이용 (FIFO)
    q = deque ()
    for i in range (len (priorities)):
        q.append ([priorities[i], i])

    locationValue = 0

    # q의 내용이 있을 때까지 반복
    while q:
        prioritiesValue, index = q.popleft ()
        # q를 pop한 후 q가 비어있는경우는 마지막 순서이기때문에 locationValue + 1을 해준다
        if len(q) == 0:
            return locationValue + 1

        # 남은 q의 최댓값이 아닐 경우에는 마지막 순위로 미룬다. (pop -> appendleft)
        if prioritiesValue < max (q)[0]:
            q.append ([prioritiesValue, index])
        # q의 최댓값이라면 index번호와 location번호 같을 때까지 반복한다. 최댓값인데 번호가 다를경우에는 앞서 pop을 했기때문에 따로 pop을 해주지 않는다. (only pop)
        else:
            locationValue += 1
            if index == location:
                return locationValue
    # 만약 loctation이 q의 길이보다 길 경우 (그럴일은 없겠지만 예외처리를 해준다)
    return -1