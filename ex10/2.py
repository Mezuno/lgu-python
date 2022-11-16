# При уч. Анастасии Самуйловой

import math

a = int(input('Введите a: '))

x = (a + 1) / (a ** 2 + math.sqrt(1 + 2 * a))
y = (a ** 2 + 1) / (a ** 4 + math.sqrt(1 + 2 * a ** 2))
z = (math.sin(a) + 1) / (math.sin(a) ** 2 + math.sqrt(1 + 2 * math.sin(a)))

print(x)
print(y)
print(z)

print(math.exp() ** (x + y + z))