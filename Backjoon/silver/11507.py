import sys
input = sys.stdin.readline


def main():
    s = input().strip()
    card = list([1] * 14 for _ in range(4))
    flag = True
    for i in range(len(s) // 3):
        tmp = s[(i * 3):(i * 3)+3]
        if tmp[0] == 'P':
            if card[0][int(tmp[1:])] == 0:
                flag = False
                break
            card[0][int(tmp[1:])] = 0
        elif tmp[0] == 'K':
            if card[1][int(tmp[1:])] == 0:
                flag = False
                break
            card[1][int(tmp[1:])] = 0
        elif tmp[0] == 'H':
            if card[2][int(tmp[1:])] == 0:
                flag = False
                break
            card[2][int(tmp[1:])] = 0
        elif tmp[0] == 'T':
            if card[3][int(tmp[1:])] == 0:
                flag = False
                break
            card[3][int(tmp[1:])] = 0

    if flag:
        res = [card[i].count(1)-1 for i in range(4)]
        print(*res)
    else:
        print("GRESKA")


main()