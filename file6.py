def even(n):
    return n % 2 == 0

a = 1
b = 4
c = -1

assert even(a) == False, 'Your code is fails!'
assert even(b) == True, 'Your code is fails!'
assert even(c) == False, 'Your code is fails!'
print('Success!')