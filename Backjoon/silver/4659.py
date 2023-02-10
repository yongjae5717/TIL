import sys
input = sys.stdin.readline


def main():
    vowel = "aeiou"

    while True:
        word = input().strip()
        if word == "end":
            break
        vow_flag = False
        dup_flag = True
        for i in range(len(word)):
            if word[i] in vowel:
                vow_flag = True
            if i > 0:
                if word[i] == word[i - 1] and word[i] != 'e' and word[i] != 'o':
                    dup_flag = False
                    break
            if i > 1:
                if word[i] not in vowel and word[i - 1] not in vowel and word[i - 2] not in vowel:
                    dup_flag = False
                    break
                elif word[i] in vowel and word[i - 1] in vowel and word[i - 2] in vowel:
                    dup_flag = False
                    break

        if vow_flag and dup_flag:
            print("<" + word + "> is acceptable.")
        else:
            print("<" + word + "> is not acceptable.")


main()