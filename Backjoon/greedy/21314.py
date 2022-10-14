import sys
input = sys.stdin.readline

input_string = list("A" + input().strip())
count = 0
min_result = ""
max_result = ""
# max_val, min_val
for i in range(len(input_string)):
    c = input_string[i]
    if c == 'M':
        count += 1
        if input_string[i-1] == 'M':
            min_result += "0"
        else:
            min_result += "1"
    elif c == 'K':
        min_result += "5"
        if count == 0:
            max_result += "5"
        else:
            max_result += str(5 * 10 ** count)
            count = 0
if count != 0:
    max_result += "1" * count


print(max_result)
print(min_result)