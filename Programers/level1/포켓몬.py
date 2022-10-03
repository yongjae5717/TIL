def solution(nums):
    pocketmon = list(set(nums))
    num = int(len(nums)/2)
    if num > len(pocketmon):
        return len(pocketmon)
    else:
        return num