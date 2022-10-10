def solution(s):
    s = s[1:-1]
    lst = s.split ("},")
    result = []
    for i in lst:
        i = i.strip ("{").strip ("}")
        temp = i.split (",")
        result.append (temp)

    result.sort (key=lambda x: len (x))
    answer = []
    for i in result:
        for j in i:
            if int (j) not in answer:
                answer.append (int (j))
    return answer