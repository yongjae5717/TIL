def solution(number, limit, power):
    primes = list()
    for i in range(1, number+1):
        if i == 1 or i == 2:
            if i <= limit:
                primes.append(i)
            else:
                primes.append(power)
        else:
            count = 0
            for j in range(1, int(i ** 0.5) + 1):
                if i % j == 0:
                    count += 1
                    if j ** 2 != i:
                        count += 1
            if count <= limit:
                primes.append(count)
            else:
                primes.append(power)
    return sum(primes)


print(solution(5, 3, 2))