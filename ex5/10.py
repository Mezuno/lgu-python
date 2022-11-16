# При уч. Анастасии Самуйловой

def F(n):
    if n == 1:
        return 1
    if n >= 2:
        return F(n - 1) + 2 ** (n - 1)
print(F(12))