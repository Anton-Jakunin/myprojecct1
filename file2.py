def func(spisok, element):
    for i in spisok:
        if i == element:
            return True
    
    return False
print(func([4, 10, 9, 8, 3], 8))