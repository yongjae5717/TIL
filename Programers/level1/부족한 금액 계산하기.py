def solution(price, money, count):
    total_price = price * sum(list(i for i in range(1, count + 1)))
    if total_price > money:
        return total_price - money
    else:
        return 0