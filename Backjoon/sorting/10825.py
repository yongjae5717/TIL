import sys

N = int(sys.stdin.readline())
array = list()
for _ in range(N):
    name, korean, english, math = sys.stdin.readline().split()
    korean = int(korean)
    english = int(english)
    math = int(math)
    array.append((name, korean, english, math))

array.sort(key=lambda x: x[0])
array.sort(key=lambda x: x[3], reverse=True)
array.sort(key=lambda x: x[2])
array.sort(key=lambda x: (x[1]), reverse=True)


for i in array:
    print(i[0])