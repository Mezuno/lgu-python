# При уч. Анастасии Самуйловой
 
def F(n):
    if n == 0:
        return 0
    if n % 3 == 2 and n > 0:
        return F(n - 1) + 1
    if n % 3 < 2:
        return F((n - n % 3) // 3)
i = 0
while F(i) != 5:
    i += 1
print(i)