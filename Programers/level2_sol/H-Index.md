# 20221009 프로그래머스

## H-Index (Level 2)
> https://school.programmers.co.kr/learn/courses/30/lessons/42747

### 문제
#### 문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

#### 제한 사항
- 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
- 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

### 구현
- 구현 알고리즘
- max, list

### 나의 답변
```python
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
```

### 코드리뷰 답변
```python
```