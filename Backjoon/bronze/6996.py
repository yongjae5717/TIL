import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        flag = True
        a, b = input().split()
        a_list = sorted(list(a))
        b_list = sorted(list(b))
        if a_list != b_list:
            flag = False

        if flag:
            print(a + " & " + b + " are anagrams.")
        else:
            print(a + " & " + b + " are NOT anagrams.")


main()