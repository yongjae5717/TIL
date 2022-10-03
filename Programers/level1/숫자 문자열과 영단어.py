def solution(s):
    answer = ''
    temp = ''
    lst = ['zero', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine']
    for i in s:
        if i.isdigit():
            answer += i
        else:
            temp += i
            if temp in lst:
                answer += str(lst.index(temp))
                temp = ''
    return int(answer)