def solution(s):
    answer = 0
    # 문자열 돌리기
    for _ in range (len (s)):
        s = s[1:] + s[0]
        if is_right (s):
            answer += 1
    return answer


# 괄호가 올바른지 아닌지 확인 (T, F)
def is_right(s):
    stack = list (s)
    stack_list = list ()

    # 리스트의 기본성질 스택을 이용하여 스택이 다 비도록 반복문 실행
    while stack:
        x = stack.pop ()
        # "]", ")", "}"이 stack_list 안에 존재할 떄, 대응되는 것이 있다면 pop, 아니라면 append 해줌
        if len (stack_list) > 0:
            if stack_list[-1] == "]" and x == "[":
                stack_list.pop ()
            elif stack_list[-1] == ")" and x == "(":
                stack_list.pop ()
            elif stack_list[-1] == "}" and x == "{":
                stack_list.pop ()
            else:
                stack_list.append (x)
        # 만약 stack_list가 없다면 x추가
        else:
            stack_list.append (x)

    # 결과: stack_list에 남는 argument가 있다면 올바르지 않은 괄호이기 때문에 False, 아니라면 True를 반환
    if len (stack_list) == 0:
        return True
    return False