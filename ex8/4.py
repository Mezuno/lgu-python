# При уч. Анастасии Самуйловой

array = [1.2, -2.3, 3.4, -4.5]
index = 0

for e in array:
    if e > 0:
        array[index] = 0
    index += 1
        
print(array)