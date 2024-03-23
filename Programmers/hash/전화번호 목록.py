def solution(phone_book):
    hash_map = {}
    for phone in phone_book:
        hash_map[phone] = 1

    for phone in phone_book:
        arr = ''
        for num in phone:
            arr += num
            if arr in hash_map and arr != phone:
                return False

    return True
