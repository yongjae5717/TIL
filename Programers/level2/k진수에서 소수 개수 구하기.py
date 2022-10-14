def solution(n, k):
    # 10진수 -> k진수로 변환한다
    temp = ""
    while n:
        temp = str (n % k) + temp
        n //= k

    # 0을 기준으로 리스트를 나눈다. (규칙)
    temp = temp.split ("0")

    answer = 0
    for i in temp:
        # 숫자가 없거나 1이하인것은 소수가 아니므로 패스
        if len (i) == 0:
            continue
        if int (i) < 2:
            continue

        # 소수판정법 이용
        prime = True
        for j in range (2, int (int (i) ** 0.5) + 1):
            if int (i) % j == 0:
                prime = False
                break
        if prime:
            answer += 1
    return answer