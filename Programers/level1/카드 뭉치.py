from collections import deque


def solution(cards1, cards2, goal):
    cards2 = list(reversed(cards2))
    card_q = deque(cards1 + cards2)
    left_cnt = len(cards1)
    right_cnt = len(cards2)

    for i in goal:
        if card_q:
            if i == card_q[0] and left_cnt > 0:
                card_q.popleft()
                left_cnt -= 1
            elif i == card_q[-1] and right_cnt > 0:
                card_q.pop()
                right_cnt -= 1
            else:
                return "No"
    return "Yes"


print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))