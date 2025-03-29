def cashe(func):
    cash = {}
    def wrapper(x, y):
        if (x, y) in cash:
            a = cash.get((x, y))
        else:
            a = func(x, y)
            cash[(x, y)] = a
        print(cash)
        return a
    return wrapper
@cashe
def stepan(x, y):
    return x ** y
print(stepan(2, 3))
print(stepan(4, 4))
print(stepan(5, 5))
stepan(345, 123456)
stepan(345, 123456)