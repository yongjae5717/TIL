import sys

test_case = int(sys.stdin.readline())
result = list()
for i in range(test_case):
    N = int(sys.stdin.readline())
    N_list = list(sys.stdin.readline().strip() for _ in range(N))
    N_list.sort()
    flag = False
    for j in range(len(N_list)-1):
        if N_list[j] in N_list[j+1][:len(N_list[j])]:
            flag = True

    if flag:
        result.append("NO")
    else:
        result.append("YES")

for i in result:
    print(i)