# При уч. Анастасии Самуйловой

array = [
    [1,2,3,4],
    [5,6,7,8],
    [9,1,2,3],
]
arrayAverage = []

for line in array:
    lineSum = 0
    elCount = 0
    
    for e in line:
        lineSum += e
        elCount += 1
    
    arrayAverage.append(lineSum/elCount)

arrayAverage = sorted(arrayAverage)

newArray = array.copy()

for line in array:
    lineSum = 0
    elCount = 0
    
    for e in line:
        lineSum += e
        elCount += 1
        
    if lineSum / elCount in arrayAverage:
        indexToWrite = arrayAverage.index(lineSum / elCount)
        newArray[indexToWrite] = line
    

print(arrayAverage)
print(newArray)