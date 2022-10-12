def solution(numbers, target):
    answer = 0
    # 시작 node: 0
    leaves = [0]
    # numbers의 순서대로 num을 빼거나 더하거나의 연산이 가능하다. 이를 leaves에 넣어준다.
    for num in numbers:
        temp = list()
        for parent in leaves:
            temp.append(parent + num)
            temp.append(parent - num)
        leaves = temp
        print(temp)

    # leaves에 모든 연산 결과가 담기기때문에 leaves의 인자 값과 target의 인자를 비교하여 같으면 카운트 증가
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer


print(solution([1,1,1,1,1], 3))