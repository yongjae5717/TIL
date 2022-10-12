from collections import deque


def solution(queue1, queue2):
    # popleft, append 사용
    s1 = sum(queue1)
    s2 = sum(queue2)

    # list -> queue로 변환
    q1 = deque(queue1)
    q2 = deque(queue2)

    # queue 당 길이
    length = len(queue1)
    # length * 3을 해준 이유는 큐 내부에서도 이동을 하기 위해서는 length만큼 길이가 더 들어간다.
    for i in range(length * 3):
        if s1 == s2:
            return i

        # s1이 크다면 q1에 있는 것을 popleft -> append해주어야 q2에 넣어준다.
        if s1 > s2:
            x = q1.popleft()
            q2.append(x)
            s1 -= x
            s2 += x
        # 반면 s2이 크다면 q2에 있는 것을 popleft -> append해주어야 q1에 넣어준다.
        elif s1 < s2:
            x = q2.popleft()
            q1.append(x)
            s1 += x
            s2 -= x
    # 전체 루프를 반복시켰는데 같은 값이 없다면 예외 처리
    return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))