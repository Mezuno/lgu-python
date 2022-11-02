# При уч. Анастасии Самуйловой

array = [
    [1.3, 2.4, 5.6],
    [3.2, 4.1, 1.1],
    [6.5, 3.2, 7.6],
]
newArray = []
elCount = 0

for line in array:
    lineSum = 0
    
    for e in line:
        lineSum += e
        elCount += 1

    newArray.append(round(lineSum/elCount, 2))
    
print(newArray)