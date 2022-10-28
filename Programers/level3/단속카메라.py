def solution(routes):
    routes.sort(key=lambda x: x[1])
    temp = -30001
    count = 0
    for r in routes:
        if r[0] > temp:
            count += 1
            temp = r[1]
    return count


print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))