"""
문자열을 이용
1. 앞에서부터 문자를 지우면서 팰린드롬 확인하기
2. 만약 지운 후의 문자의 길이가 1이면 원래의 문자길이 * 2 -1
3. 아니라면 팰린드롬일 경우의 index 값을 더해준다.
"""


import sys


def is_pal(input_string):
    temp = len(input_string)
    for i in range(len(input_string)):
        set_string = input_string[i:]  # 앞 문자열 하나씩 제거하면서 확인
        if len(set_string) == 1 or set_string == set_string[::-1]:
            return temp + i


S = sys.stdin.readline().strip()
print(is_pal(S))