def solution(prices):
    answer = []
    for i in range(len(prices)):
        price = prices[i]
        time = 0
        for j in range(i+1, len(prices)):
            time += 1
            if price > prices[j]:
                break
        answer.append(time)
    return answer