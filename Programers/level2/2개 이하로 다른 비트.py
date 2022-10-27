def solution(numbers):
    answer = []

    for i in numbers:
        binary = list("0" + bin(i)[2:])
        # rfind: 오른쪽부터 index찾아주기
        idx = "".join(binary).rfind("0")
        binary[idx] = "1"

        # 홀수의 경우 예외처리
        if i % 2 == 1:
            binary[idx + 1] = "0"

        answer.append(int("".join(binary), 2))
    return answer


print(solution([2, 7]))