def solution(arr):
    arr.remove(min(arr))
    if arr:
        return arr
    return [-1]