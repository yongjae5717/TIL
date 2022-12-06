def solution(n):
    triangle = list(list(0 for _ in range(1, i+1)) for i in range(1, n+1))

    x, y = -1, 0
    number = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            triangle[x][y] = number
            number += 1
    return sum(triangle, list())


print(solution(4))
print(solution(5))
print(solution(6))