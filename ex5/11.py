# При уч. Анастасии Самуйловой

def F(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    if n > 3:
        return F(n-3) + F(n-2) + F(n-1)
print(F(9))