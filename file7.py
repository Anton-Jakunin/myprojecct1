def is_palindrome(s):
    tmp = s
    tmp.reverse()

    if tmp == s:
        return True
    else:
        return False

def word(n):
    result = []
    for i in range(n):
        element = input('Enter element: ')
        result.append(element)
        if is_palindrome(result):
            print(f'{result} - is palindrome')
        else:
            print(f'{result} - not a palindrome')

word(5)