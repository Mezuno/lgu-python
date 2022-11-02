# При уч. Анастасии Самуйловой

array = [1,2,3,4,5,6,7,8]
index = 1
C = 3

for e in array:
    if e > C:
        resultElementNumber = index
        resultElementValue = e
        break
        
    index += 1

print('Номер элемента: ', resultElementNumber)
print('Значение элемента: ', resultElementValue)