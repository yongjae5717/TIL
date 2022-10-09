from collections import deque


def solution(cacheSize, cities):
    # queue를 이용하여 구현
    q = deque()
    # 결과값
    answer = 0

    for i in cities:
        # 대소문자 구분이 없다는 조건
        i = i.lower()
        # 캐시 사이즈만큼 queue에 넣어줌(왼쪽부터 차례대로)
        if cacheSize != 0:
            # 캐시에 없을 경우에는 왼쪽부터 추가
            if i not in q:
                answer += 5
                q.appendleft(i)
                cacheSize -= 1
            # 캐시에 존재할 경우 존재하는 단어를 가장 왼쪽으로 이동
            else:
                answer += 1
                LRU(q, i)
        # 캐시 사이즈가 모두 찼을 경우
        else:
            # 캐시에 없을 경우에는 왼쪽부터 추가
            if i not in q:
                answer += 5
                q.appendleft(i)
                q.pop()
            # 캐시에 존재할 경우 존재하는 단어를 가장 왼쪽으로 이동
            else:
                answer += 1
                LRU(q, i)
    return answer


# 최근 캐시에서 사용한 단어를 가장 왼쪽 queue에 넣어주는 함수 (나머지의 순서는 동일)
def LRU(queue, word):
    l = len(queue)
    x = queue.pop()
    while x != word:
        queue.appendleft(x)
        x = queue.pop()
        l -= 1
    for _ in range(l-1):
        y = queue.pop()
        queue.appendleft(y)
    queue.appendleft(x)