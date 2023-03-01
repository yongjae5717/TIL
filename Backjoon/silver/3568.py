import sys, re
input = sys.stdin.readline


def main():
    lst = list(input().replace(",", "").replace(";", "").split())
    variable = lst[0]

    for s in lst[1:]:
        tmp = variable
        reversed_s = list(reversed(s))
        for i in range(len(s)):
            if not reversed_s[i].isalpha():
                if reversed_s[i] == ']':
                    tmp += '['
                elif reversed_s[i] == '[':
                    tmp += ']'
                else:
                    tmp += reversed_s[i]
        var = re.findall('[a-zA-Z]+', s)
        print(tmp, "".join(var) + ";")



main()