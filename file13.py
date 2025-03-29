def poisk(spisok, chislo):
    for i in spisok:
        if i == chislo:
            return True
    return False
print(poisk([4, 5, 7, 8, 10], 8))    