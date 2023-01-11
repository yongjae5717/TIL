def main():
    while True:
        line = input()
        stack = []

        if line == ".":
            break

        for i in line:
            if i == '[' or i == '(':
                stack.append(i)

            elif i == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')
                    break

            elif i == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(']')
                    break

        if stack:
            print('no')
        else:
            print('yes')


main()