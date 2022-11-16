# При уч. Анастасии Самуйловой

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

ab = [a, b]
abc = [a, b, c]
bc = [b, c]
aplusbc = [int(a) + int(b), c]

u = (max(abc) + min(aplusbc)) / (max(bc) * min(abc) * max(ab))

print(u)
