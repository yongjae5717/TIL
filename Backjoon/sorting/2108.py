import sys

# 1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

N = int(sys.stdin.readline())
array = list()
function = [0, 0, 0, 0]
for _ in range(N):
    array.append(int(sys.stdin.readline()))

function[0] = round(sum(array) / N)
array.sort()
function[1] = array[len(array) // 2]

dictionary = dict()
for i in array:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1
frequency = list()
for j in dictionary:
    if dictionary[j] == max(dictionary.values()):
        frequency.append(j)
frequency.sort()


if len(frequency) != 1:
    function[2] = frequency[1]
else:
    function[2] = frequency[0]

function[3] = max(array) - min(array)

for k in function:
    print(k)