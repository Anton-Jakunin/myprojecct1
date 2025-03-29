a = int(input('Введите число:'))
b = int(input('Введите число:'))
A = []
for i in range(a):
    B = []
    for j in range(b):
        if (i + j) % 2 == 0:
            B.append('.')
        else:
            B.append('*')
    A.append(B)
print(A)