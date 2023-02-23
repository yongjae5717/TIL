import sys, re
from functools import cmp_to_key
input = sys.stdin.readline
alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"


def main():
    n = int(input())
    words = list()
    for _ in range(n):
        tmp = input().strip()
        words.append([tmp, re.findall("[a-zA-Z]|\d+", tmp)])
    words.sort(key=cmp_to_key(comp))

    for word in words:
        print(word[0])


def comp(first, second):
    for i in range(min(len(first[1]), len(second[1]))):
        # 숫자가 우선순위
        if first[1][i].isdigit() and second[1][i].isalpha():
            return -1
        # 숫자가 우선순위
        elif first[1][i].isalpha() and second[1][i].isdigit():
            return 1
        # 둘다 숫자의 경우
        elif first[1][i].isdigit() and second[1][i].isdigit():
            if int(first[1][i]) == int(second[1][i]):
                # 같은 숫자면 패스
                if len(first[1][i]) == len(second[1][i]):
                    continue
                # 0의 개수가 많으면 양수, 적으면 음수 반환
                return len(first[1][i]) - len(second[1][i])
            else:
                # first가 크면 양수 second가 크면 음수 반환
                return int(first[1][i]) - int(second[1][i])
        # 둘다 문자의 경우
        else:
            # 같은 문자면 패스
            if first[1][i] == second[1][i]:
                continue
            else:
                # 알파벳의 인덱스를 비교하여 양수 음수 반환
                return alphabet.index(first[1][i]) - alphabet.index(second[1][i])
    # 앞 문자가 같은 경우 길이 비교
    return len(first[1]) - len(second[1])


main()