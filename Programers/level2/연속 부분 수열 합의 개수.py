def solution(elements):
    length = len(elements)
    elements += elements
    answer = set()
    for i in range(1, length+1):
        for j in range(length):
            s = sum(elements[j:j+i])
            answer.add(s)
    return len(answer)


print(solution([7,9,1,1,4]))