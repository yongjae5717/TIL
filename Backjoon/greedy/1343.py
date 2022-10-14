import sys

board = sys.stdin.readline().strip()
count = 0
result = list()
for i in range(len(board)):
    if board[i] == '.':
        count = 0
        result.append(count)
    elif board[i] == 'X':
        count += 1
        result.append(count)
    else:
        board = "X" + "." * (len(board) - 1)

# print(result)

ans = ""
if result[0] == 0:
    ans += "."

for i in range(1, len(result)):
    if result[i] == 0 and (result[i-1] % 4 == 2):
        ans += "AAAA" * (result[i-1] // 4) + "BB" * ((result[i-1] % 4) // 2) + "."
    elif result[i] == 0 and (result[i-1] % 4 == 0):
        ans += "AAAA" * (result[i-1] // 4) + "."
    elif result[i] == 0 and (result[i-1] == 0):
        ans += "."

if result[len(result) - 1] > 0 == result[len(result) - 1] % 2:
    ans += "AAAA" * (result[len(result) - 1] // 4) + "BB" * ((result[len(result) - 1] % 4) // 2)


# print(ans)
if len(ans) == len(board):
    print(ans)
elif 'X' not in board:
    print(board)
else:
    print(-1)