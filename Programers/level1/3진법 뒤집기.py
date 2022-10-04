def solution(n):
    answer = 0
    lst = list ()
    # 3진법 표기 + 앞뒤 반전
    while n >= 1:
        lst.append (int (n % 3))
        n = (n - n % 3) / 3

    # 10진법으로 변환
    for i in range (len (lst)):
        answer += lst[len (lst) - i - 1] * (3 ** i)
    return answer
