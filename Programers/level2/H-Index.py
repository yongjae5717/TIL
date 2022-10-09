def solution(citations):
    n = len(citations)
    answer = 0
    # 논문의 수: 0 ~ n
    for h in range(n+1):
        count = 0
        # 논문 당 인용 수: i
        for i in citations:
            # 인용수가 기준보다 높을 경우
            if i >= h:
                count += 1
        # h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다.
        if count >= h:
            # h의 최댓값을 구하는 것
            answer = max(answer, h)
    return answer


lst = [1, 4]
print(solution(citations=lst))