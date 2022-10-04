def solution(N, stages):
    level = [0] * (N + 1)

    # 스테이지의 개수가 1개 예외 설정
    if N == 1:
        return [1]

    # 스테이지 별 인원 설정
    for i in stages:
        for i in range (i):
            level[i] += 1

    answer = []
    for i in range (1, N + 1):
        # 분모가 0일 경우 예외처리
        if level[i - 1] == 0:
            success = 1
        else:
            # 성공률은 현재 스테이지 성공한 사람 / 이전 스테이지 성공한 사람
            success = level[i] / level[i - 1]
        # 실패율은 1-성공률
        answer.append ([1 - success, i])
    # 실패율은 내림차순, 실패율이 같다면 오름차순
    answer.sort (key=lambda x: (-x[0], x[1]))

    result = list ()
    for i in range (N):
        x, y = answer[i]
        result.append (y)

    return result