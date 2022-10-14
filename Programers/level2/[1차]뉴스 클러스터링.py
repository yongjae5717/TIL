from collections import Counter


def solution(str1, str2):
    # str1을 다중집합으로 변환
    lst1 = []
    for i in range(1, len(str1)):
        if str1[i-1].isalpha() and str1[i].isalpha():
            lst1.append(str1[i-1].lower() + str1[i].lower())

    # str2을 다중집합으로 변환
    lst2 = []
    for i in range(1, len(str2)):
        if str2[i-1].isalpha() and str2[i].isalpha():
            lst2.append(str2[i-1].lower() + str2[i].lower())

    # Counter을 이용하여 같은 문자가 몇번 있는지 확인
    Counter1 = Counter(lst1)
    Counter2 = Counter(lst2)

    # 교집합
    inter = list((Counter1 & Counter2).elements())
    # 합집합
    union = list((Counter1 | Counter2).elements())

    # 만약 둘다 공집합이면 나누는 것이 안되기때문에 65536 return
    if len(inter) == 0 and len(union) == 0:
        return 65536

    # 일반적인 경우
    return int(len(inter)/len(union) * 65536)


print(solution("aa1+aa2", "AAAA12"))