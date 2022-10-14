import sys

N = int(sys.stdin.readline())
books = list(sys.stdin.readline().strip() for i in range(int(N)))
books.sort()
dictionary = dict()
for i in books:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1

# print(max(dictionary.values()))

for j in dictionary:
    if dictionary[j] == max(dictionary.values()):
        print(j)
        break