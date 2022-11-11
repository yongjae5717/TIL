def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    result = 0
    while B:
        if A[-1] < B[-1]:
            A.pop()
            B.pop()
            result += 1
        else:
            B.pop()
    return result


print(solution([5,1,3,7], [2,2,6,8]))  # 3
print(solution([2,2,2,2], [1,1,1,1]))  # 0