def solution(clothes):

    # dictionary를 이용하여 key를 종류, value를 옷의 갯수로 넣어주었습니다.
    clothesDict = dict()
    for cloth in clothes:
        if cloth[1] not in clothesDict:
            clothesDict[cloth[1]] = 1  # 1이라고 해준 것은 안입는 경우
        clothesDict[cloth[1]] += 1

    # 종류별 옷의 갯수를 모두 곱합니다.
    answer = 1
    for i in clothesDict.values():
        answer *= i

    return answer - 1  # -1을 해준 이유는 옷 종류 모두를 안입는 경우


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))