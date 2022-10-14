import sys
input = sys.stdin.readline

n = int(input())
place = list(map(int, input().split()))
sum_place = sum(place)

# bee bee honey
b_b_h = 0
bee = place[0]
for i in range(1, n):
    bee += place[i]
    first_bee = sum_place - place[0] - place[i]  # 첫번째 벌이 먹는 꿀의 양
    second_bee = sum_place - bee  # 두번째 벌이 먹는 꿀의 양
    b_b_h = max(b_b_h, first_bee + second_bee)


# honey bee bee
h_b_b = 0
place.reverse()
bee = place[0]
for j in range(1, n):
    bee += place[j]
    first_bee = sum_place - place[0] - place[j]  # 첫번째 벌이 먹는 꿀의 양
    second_bee = sum_place - bee  # 두번째 벌이 먹는 꿀의 양
    h_b_b = max(h_b_b, first_bee + second_bee)


# bee honey bee
b_h_b = 0
for k in range(1, n):
    b_h_b = max(b_h_b, sum_place - place[0] - place[n-1] + place[k])

print(max(b_b_h, b_h_b, h_b_b))