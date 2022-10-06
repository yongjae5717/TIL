def solution(id_list, report, k):
    answer = []

    # id_list의 index를 기준으로 index를 구분하기 위한 dictionary를 구성
    index = dict()
    for i in range (len (id_list)):
        key = id_list[i]
        index[key] = i

    # 신고 당한 횟수와 유저별로 신고를 한 리스트 전체
    idValue = [0] * len (id_list)
    forbiddenList = [[] for _ in range (len (id_list))]

    # report에서 유저와 유저가 신고한 유저에 대한 정보를 list로 구성
    for i in report:
        userId, forbiddenId = i.split ()
        idx = index[userId]
        idx2 = index[forbiddenId]
        # 중복을 허용하지 않기 위함
        if forbiddenId not in forbiddenList[idx]:
            idValue[idx2] += 1
            forbiddenList[idx].append (forbiddenId)

    # 유저가 신고를 한 리스트 중에서 k보다 큰 신고한 ID만 count에 추가시켜 answer로 return
    for i in forbiddenList:
        count = 0
        for j in i:
            idx = index[j]
            if idValue[idx] >= k:
                count += 1
        answer.append(count)
    return answer