import sys
input = sys.stdin.readline

input_string = list(input().strip())
stack = list()
ans = 0
count = 1
primary_value = 0

for i in input_string:
    if i == '(':
        count *= 2
        stack.append(i)
    elif i == '[':
        count *= 3
        stack.append(i)
    elif i == ')':
        # 올바른 괄호열이 아닐 경우
        if not stack or stack[-1] == '[':
            ans = 0
            break
        elif primary_value == '(':
            ans += count
        count //= 2
        stack.pop()
    elif i == ']':
        # 올바른 괄호열이 아닐경우
        if not stack or stack[-1] == '(':
            ans = 0
            break
        elif primary_value == '[':
            ans += count
        count //= 3
        stack.pop()
    primary_value = i

if stack:
    print(0)
else:
    print(ans)