def solution(arr1, arr2):
    result = list()
    for a, b in zip(arr1, arr2):
        temp = list()
        for x, y in zip(a, b):
            temp.append(x + y)
        result.append(temp)
    return result