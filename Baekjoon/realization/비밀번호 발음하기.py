vowels = {'a','e','i','o','u'}
alphabet = {chr(i) for i in range (ord('a'), ord('z')+1) }
consonants = alphabet-vowels


def check(arr):
    v = 0
    c = 0
    for i in range(len(arr)):
        if i !=0 and arr[i] == arr[i-1]:
            if arr[i] != 'e' and arr[i] != 'o':
                return False
        if arr[i] in vowels:
            v += 1
            c = 0
        if arr[i] in consonants:
            c += 1
            v = 0
        if v >= 3 or c >= 3:
            return False
    return True


while True:
    arr = input()
    if arr == 'end':
        break

    if len(set(arr) & vowels) >= 1 and check(arr) :
        print(f'<{arr}> is acceptable.')
    else:
        print(f'<{arr}> is not acceptable.')
