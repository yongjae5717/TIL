def solution(phone_book):
    phone_book.sort()
    for x, y in zip(phone_book, phone_book[1:]):
        if x == y[:len(x)]:
            return False
    return True


phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))