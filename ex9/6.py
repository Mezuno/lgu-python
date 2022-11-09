# При уч. Анастасии Самуйловой

for num in range(95632, 95651):
    deliteli = []
    for d in range(1, int(num**0.5) + 1):
        if num % d == 0:
            if d % 2 != 0:
                deliteli.append(d)
            if num // d != d and num // d % 2 != 0:
                deliteli.append(num // d)
    if len(deliteli) == 6:
        deliteli.sort()
        print(deliteli[0], deliteli[1], deliteli[2], deliteli[3], deliteli[4], deliteli[5])