import sys
import heapq

score = list()
for i in range(8):
    heapq.heappush(score, (int(sys.stdin.readline()), i+1))
heapq.heappop(score)
heapq.heappop(score)
heapq.heappop(score)
score.sort(key=lambda x: x[1])
sum_score = 0
result = ""
for j in range(len(score)):
    result += str(score[j][1]) + " "
    sum_score += score[j][0]
print(sum_score)
print(result)