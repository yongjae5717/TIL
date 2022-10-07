def solution(n):
    onesCount = str(bin(n))[2:].count("1")
    while True:
        n += 1
        tempOnesCount = str(bin(n))[2:].count("1")
        if tempOnesCount == onesCount:
            return n


print(solution(78))