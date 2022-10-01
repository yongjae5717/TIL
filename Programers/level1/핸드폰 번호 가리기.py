def solution(phone_number):
    star_len = len(phone_number) - 4
    find_numbers = phone_number[star_len:]
    return "*" * star_len + find_numbers