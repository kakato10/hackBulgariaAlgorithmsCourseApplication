def search_palindroms(word):
    count = 0
    for i in range(0, len(word)):
        variation = word[i:] + word[0:i]
        if is_palindrom(variation):
            print(variation)
            count = count + 1
    if count == 0:
        print('NONE')


def is_palindrom(word):
    return word == word[::-1]
