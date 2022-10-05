def solution(lottos, win_nums):
    zeroCount, correctCount, maxValue, minValue = 0, 0, 0, 0
    for i in lottos:
        if i == 0:
            zeroCount += 1
        else:
            if i in win_nums:
                correctCount += 1

    maxValue = min (6, 7 - (correctCount + zeroCount))
    if correctCount == 0 or correctCount == 1:
        minValue = 6
    else:
        minValue = 7 - correctCount

    return [maxValue, minValue]


def solution2(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
